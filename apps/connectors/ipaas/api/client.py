import time
from typing import List, Optional, Dict, Any

import jwt
import requests

from apps.connectors.base.models import Integration
from chimera import settings


class IntegrationAppClient:
    def __init__(
        self,
        workspace_key: str = settings.IPAAS_WORKSPACE_KEY,
        secret_or_private_key: str = settings.IPAAS_WORKSPACE_SECRET,
        algorithm: str = "HS512",
        base_url: str = settings.IPAAS_BASE_URL,
    ):
        self.workspace_key = workspace_key
        self.secret_or_private_key = secret_or_private_key
        self.algorithm = algorithm
        self.base_url = base_url
        self._token_cache: Dict[str, str] = {}

    def generate_token(
        self,
        *,
        user_id: Optional[str] = None,
        user_name: Optional[str] = None,
        fields: Optional[Dict[str, Any]] = None,
        is_admin: bool = False,
        expires_in: int = settings.IPAAS_WORKSPACE_TOKEN_EXPIRATION_SECONDS,
    ) -> str:
        now = int(time.time())
        payload = {"iat": now, "exp": now + expires_in, "iss": self.workspace_key}

        if is_admin:
            payload["isAdmin"] = True
        else:
            if not user_id or not user_name:
                raise ValueError("user_id and user_name are required for user token")
            payload.update({"id": user_id, "name": user_name, "fields": fields or {}})

        return jwt.encode(payload, self.secret_or_private_key, algorithm=self.algorithm)

    def with_user_context(
        self,
        user_id: str,
        user_name: str,
        fields: Optional[Dict[str, Any]] = None,
        expires_in: int = settings.IPAAS_WORKSPACE_TOKEN_EXPIRATION_SECONDS,
        use_cache: bool = False,
    ):
        cache_key = f"user:{user_id}"
        if use_cache and cache_key in self._token_cache:
            token = self._token_cache[cache_key]
        else:
            token = self.generate_token(
                user_id=user_id,
                user_name=user_name,
                fields=fields,
                is_admin=False,
                expires_in=expires_in,
            )
            if use_cache:
                self._token_cache[cache_key] = token

        return self.with_token_context(token)

    def with_admin_context(
        self, expires_in: int = settings.IPAAS_WORKSPACE_TOKEN_EXPIRATION_SECONDS
    ):
        token = self.generate_token(is_admin=True, expires_in=expires_in)
        return self.with_token_context(token)

    def with_token_context(self, token: str) -> "_ScopedIntegrationAppSession":
        """
        Create a session with a pre-generated token.
        This is useful for scenarios where the token is already available.
        """
        return _ScopedIntegrationAppSession(self, token)


class _ScopedIntegrationAppSession:
    def __init__(self, client: IntegrationAppClient, token: str):
        self.client = client
        self.token = token

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Optionally clear token or perform logging here.
        pass

    def _get_headers(self) -> Dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"}

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        url = f"{self.client.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.client.base_url}/{endpoint.lstrip('/')}"
        response = requests.post(url, headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    # Add put, delete, etc. as needed
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.client.base_url}/{endpoint.lstrip('/')}"
        response = requests.put(url, headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> Dict[str, Any]:
        url = f"{self.client.base_url}/{endpoint.lstrip('/')}"
        response = requests.delete(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json() if response.content else {}

    def list_integrations(self, integration_names: List[str]) -> List[Integration]:
        response = self.get(
            "integrations", params={"search": "|".join(integration_names)}
        )
        return [
            Integration(**integration)
            for integration in response.get("items")
            if integration["key"] in integration_names
        ]


integration_appi_client = IntegrationAppClient()


def get_integration_app_client() -> IntegrationAppClient:
    return integration_appi_client
