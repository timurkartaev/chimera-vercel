import datetime
from typing import Any, Optional
import uuid

import jwt
from django.conf import settings
from urllib.parse import urlencode

from pydantic import BaseModel
from enum import StrEnum
import logging
from django_eventstream import send_event

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class AuthConfig(BaseModel):
    auth_method: str
    auth_params: Optional[list[dict[str, Any]]] = None
    base_connection_url: str


class CallbackState(StrEnum):
    SUCCESS = "success"
    ERROR = "error"
    CANCELLED = "cancelled"
    IN_PROGRESS = "in_progress"


class AuthenticateCapability:

    def __init__(self, config, api_client):
        self.config = config

    def get_authentication_config(self, customer: dict[str, Any]) -> AuthConfig:

        return AuthConfig(
            auth_method=self.config.authentication.auth_method,
            auth_params=self.config.authentication.auth_params,
            base_connection_url=self.get_authentication_url(customer),
        )

    def get_authentication_url(self, customer) -> str:
        params = self.make_params(customer)
        return f"{settings.IPAAS_BASE_URL}/connection-popup?{urlencode(params)}"

    def make_params(self, customer):
        params = {
            "integrationKey": self.config.info.slug,
            "token": self.build_token(customer),
            "requestId": uuid.uuid4(),
        }
        return params

    def build_token(self, customer):
        return jwt.encode(
            {
                "id": customer["id"],
                "name": customer["name"],
                "iss": settings.IPAAS_WORKSPACE_KEY,
                "fields": {},
                "exp": datetime.datetime.now()
                + datetime.timedelta(
                    minutes=settings.IPAAS_WORKSPACE_TOKEN_EXPIRATION_MINUTES
                ),
            },
            settings.IPAAS_WORKSPACE_SECRET,
            algorithm="HS256",
        )

    def handle_callback(self, request):
        """Handle the callback from the authentication process."""
        query_params = request.GET.dict()
        state = CallbackState.SUCCESS
        redirect_uri = None
        if "error" in query_params and query_params["error"] == "access_denied":
            state = CallbackState.CANCELLED
        elif "error" in query_params:
            state = CallbackState.ERROR
        elif "code" in query_params and "state" in query_params:
            state = CallbackState.IN_PROGRESS
        if state == CallbackState.IN_PROGRESS:
            redirect_uri = (
                f"{settings.IPAAS_BASE_URL}/oauth-callback?{urlencode(query_params)}"
            )
        send_event(
            "status",
            "message",  
            {
                "status": state.value,
                "requestId": query_params.get("requestId"),
            },
            async_publish=False
        )
        return state, redirect_uri
