from typing import Any, Dict, List, Optional, Tuple
import uuid

from django.conf import settings
from urllib.parse import urlencode

from pydantic import BaseModel
from enum import StrEnum

from apps.connectors.base.capability import (
    BaseAuthorizeCapability,
    BaseAuthorizeBegin,
    BaseAuthorizeFinalize,
    BaseGetIntegrationStatus,
)
from apps.connectors.base.connector import ConnectorConfig
from apps.connectors.ipaas.api.client import IntegrationAppClient


class AuthorizationStatus(StrEnum):
    SUCCESS = "success"
    ERROR = "error"
    CANCELLED = "cancelled"


class IpaasAuthorizeBegin(BaseAuthorizeBegin):
    def execute(
        self,
        input_model: BaseAuthorizeBegin.Input,
        context: "AuthorizeCapability",
    ) -> BaseAuthorizeBegin.Output:
        token = context.client.generate_token(
            user_id=input_model.customer_id, user_name=input_model.customer_name
        )
        integration_key = context.config.info.slug
        params = {
            "integrationKey": integration_key,
            "token": token,
            "requestId": uuid.uuid4(),
        }
        with context.client.with_token_context(token) as session:
            response = session.get(f"integrations/{integration_key}")
            auth_method, auth_params = self.get_auth_type_and_params(response)

        auth_url = context.client.base_url + "/connection-popup?" + urlencode(params)
        return BaseAuthorizeBegin.Output(
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


class IpaasAuthorizeFinalize(BaseAuthorizeFinalize):
    def execute(
        self,
        input_model: BaseAuthorizeFinalize.Input,
        context: "AuthorizeCapability",
    ) -> BaseAuthorizeFinalize.Output:
        status = AuthorizationStatus.SUCCESS
        error_message = None
        if not input_model.code or not input_model.state:
            status = AuthorizationStatus.ERROR
            error_message = "Missing required parameters: 'code' or 'state'."
        elif input_model.error and input_model.error != "access_denied":
            status = AuthorizationStatus.ERROR
            error_message = input_model.errore
        elif input_model.error == "access_denied":
            status = AuthorizationStatus.CANCELLED
            error_message = "User cancelled the authorization process."

        query_params = input_model.model_dump(exclude_none=True)
        redirect_uri = (
            f"{settings.IPAAS_BASE_URL}/oauth-callback?{urlencode(query_params)}"
        )
        return BaseAuthorizeFinalize.Output(
            status=status.value,
            redirect_uri=redirect_uri,
            error_message=error_message,
        )



class AuthorizeCapability(BaseAuthorizeCapability):

    begin = IpaasAuthorizeBegin("Begin Authorization")
    finalize = IpaasAuthorizeFinalize("Finalize Authorization")
    get_integration_status = IpaasGetIntegrationStatus("Get Integration Status")

    def __init__(self, config: ConnectorConfig, client: IntegrationAppClient):
        self.config = config
        self.client = client
