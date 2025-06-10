import json
from typing import Any, Dict, List, Optional
import uuid

from django.conf import settings
from urllib.parse import urlencode

from enum import StrEnum

from apps.connectors.base.capability import (
    AuthorizeGetStatus,
    BaseAuthorizeCapability,
    AuthorizeBegin,
    AuthorizeFinalize,
)
from apps.connectors.base.connector import ConnectorConfig
from apps.connectors.ipaas.api.client import IntegrationAppClient
from cachetools import TTLCache

authorization_cache = TTLCache(maxsize=100, ttl=5 * 60)


class AuthorizationStatus(StrEnum):
    SUCCESS = "success"
    ERROR = "error"
    CANCELLED = "cancelled"
    PENDING = "pending"


class IpaasAuthorizeBeginCapabilityAction(AuthorizeBegin):
    def execute(
        self,
        input_model: AuthorizeBegin.Input,
        context: "AuthorizeCapability",
    ) -> AuthorizeBegin.Output:
        token = context.client.generate_token(
            user_id=input_model.customer_id, user_name=input_model.customer_name
        )
        integration_key = context.config.info.slug
        request_id = uuid.uuid4()
        authorization_cache[request_id] = {
            "status": AuthorizationStatus.PENDING.value,
            "request_id": request_id,
            "error_message": None,
        }
        params = {
            "integrationKey": integration_key,
            "token": token,
            "requestId": request_id,
        }

        with context.client.with_token_context(token) as session:
            response = session.get(f"integrations/{integration_key}")
            auth_method, auth_params = self.get_auth_type_and_params(response)

        if auth_method == "credentials":
            params["redirectUri"] = (
                f"{settings.BASE_URL}/auth/{integration_key}/callback?requestId={request_id}"
            )

        auth_url = context.client.base_url + "/connection-popup?" + urlencode(params)
        return AuthorizeBegin.Output(
            auth_url=auth_url,
            auth_method=auth_method,
            auth_params=auth_params,
        )

    @classmethod
    def get_auth_type_and_params(
        cls,
        integration_details: dict[str, Any],
    ) -> tuple[str, Optional[list[dict[str, Any]]]]:
        auth_type = integration_details.get("authType", "oauth2")
        auth_params = []
        auth_options = integration_details.get("authOptions", None)
        auth_option = next(
            (option for option in auth_options if option.get("type") == auth_type),
            auth_options[0],
        )

        if not auth_option:
            raise ValueError(f"No auth option found for type: {auth_type}")

        properties = auth_option.get("ui", {}).get("schema", {}).get("properties", {})
        required_fields = (
            auth_option.get("ui", {}).get("schema", {}).get("required", [])
        )
        if properties:
            auth_params = [
                {
                    "id": key,
                    "label": value.get("title", " ".join(key.split("_")).title()),
                    "type": value.get("type", "string"),
                    "default": value.get("default", None),
                    "required": key in required_fields,
                }
                for key, value in properties.items()
            ]

        return cls.rename_auth_type(auth_type, auth_params), auth_params

    @staticmethod
    def rename_auth_type(auth_type: str, auth_params: List[Dict[str, Any]]) -> str:
        """
        Rename the auth type to match the expected format.
        """
        if auth_type == "oauth2" and auth_params:
            return "oauth2+fields"
        if auth_type == "client-credentials":
            return "credentials"
        return auth_type


class IpaasAuthorizeFinalizeCapabilityAction(AuthorizeFinalize):
    def execute(
        self,
        input_model: AuthorizeFinalize.Input,
        context: "AuthorizeCapability",
    ) -> AuthorizeFinalize.Output:
        status = AuthorizationStatus.PENDING.value
        connection_id = getattr(input_model, "connectionId", None)
        error = getattr(input_model, "error", None)
        error_data = getattr(input_model, "errorData", None)
        request_id = getattr(input_model, "requestId", None)
        if error_data:
            error_data = json.loads(error_data)
        is_from_ipaas = connection_id is not None or error_data is not None
        if is_from_ipaas:
            # This is the final callback from iPaaS (success or failure)
            status = AuthorizationStatus.SUCCESS.value
            error_message = None

            if error:
                status = AuthorizationStatus.ERROR.value
                error_message = self.get_error_message(error, error_data)
            if request_id:
                authorization_cache[request_id] = {
                    "status": status,
                    "request_id": request_id,
                    "error_message": error_message,
                }
            return IpaasAuthorizeFinalizeCapabilityAction.Output(
                status=status,
                redirect_uri=None,
                error_message=error_message,
            )

        # Otherwise, this is a callback from the OAuth provider — redirect to iPaaS
        query_params = input_model.model_dump(exclude_none=True)
        # query_params.pop("redirectUri", None)  # Prevent redirect loop

        redirect_uri = (
            f"{settings.IPAAS_BASE_URL}/oauth-callback?{urlencode(query_params)}"
        )

        authorization_cache[input_model.requestId] = {
            "status": status,
            "error_message": error_message,
            "request_id": input_model.requestId,
        }
        return IpaasAuthorizeFinalizeCapabilityAction.Output(
            status=status,
            redirect_uri=redirect_uri,
            error_message=None,
        )

    def get_error_message(self, error: str, error_data: dict[str, Any]) -> str:
        try:
            if "data" in error_data:
                if "response" in error_data["data"]:
                    return error_data["data"]["response"]["data"]["error"]["message"]
        except Exception as e:
            return error
        return error


class IpaasAuthorizeGetStatusCapabilityAction(AuthorizeGetStatus):
    def execute(
        self,
        input_model: AuthorizeGetStatus.Input,
        context: "AuthorizeCapability",
    ) -> AuthorizeGetStatus.Output:
        if input_model.request_id not in authorization_cache:
            return IpaasAuthorizeGetStatusCapabilityAction.Output(
                status=AuthorizationStatus.PENDING.value,
                error_message=None,
            )
        return IpaasAuthorizeGetStatusCapabilityAction.Output(
            status=authorization_cache[input_model.request_id]["status"],
            error_message=authorization_cache[input_model.request_id]["error_message"],
        )


class AuthorizeCapability(BaseAuthorizeCapability):
    begin = IpaasAuthorizeBeginCapabilityAction("Begin Authorization")
    finalize = IpaasAuthorizeFinalizeCapabilityAction("Finalize Authorization")
    get_status = IpaasAuthorizeGetStatusCapabilityAction("Get Authorization Status")

    def __init__(self, config: ConnectorConfig, client: IntegrationAppClient):
        self.config = config
        self.client = client
