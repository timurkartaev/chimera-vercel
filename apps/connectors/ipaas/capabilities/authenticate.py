import datetime
from typing import Any, Optional
import uuid

import jwt
from django.conf import settings
from urllib.parse import urlencode

from pydantic import BaseModel


class AuthConfig(BaseModel):
    auth_method: str
    auth_params: Optional[list[dict[str, Any]]] = None
    base_connection_url: str


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
        if self.config.authentication.auth_method == "oauth2":
            params["redirectUri"] = self.config.authentication.oauth2.redirect_url
        return params

    def build_token(customer):
        return jwt.encode(
            {
                "id": customer.id,
                "name": customer.name,
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
