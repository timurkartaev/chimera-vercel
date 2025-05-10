import requests
import json
import logging
from requests.exceptions import RequestException, Timeout
from ..utils.helpers import retry_with_backoff
from typing import Dict, Any, Optional, Union

logger = logging.getLogger(__name__)

class ApiClient:
    """
    Base API client for making HTTP requests to external systems.
    This is a thin wrapper around HTTP operations with no business logic.
    """
    
    def __init__(self, base_url: Optional[str] = None, auth_token: Optional[str] = None):
        """Initialize the API client.

        Args:
            base_url: Base URL for API requests.
            auth_token: Authentication token.
        """
        self._session = requests.Session()
        self._base_url = base_url
        self._auth_token = auth_token
        self.refresh_token = None
        self.auth_metadata = {}
    
    def set_base_url(self, base_url: str):
        """Set the base URL for API requests."""
        self._base_url = base_url
    
    def set_auth_token(self, auth_token: str):
        """Set the authentication token."""
        self._auth_token = auth_token
    
    def set_refresh_token(self, refresh_token: str):
        """Set the refresh token."""
        self.refresh_token = refresh_token
    
    def set_auth_metadata(self, metadata: dict):
        """Set the authentication metadata."""
        self.auth_metadata = metadata
    
    @property
    def auth_token(self) -> Optional[str]:
        """Get the current authentication token."""
        return self._auth_token
    
    def _get_headers(self) -> Dict[str, str]:
        """Get the headers for API requests."""
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        if self._auth_token:
            headers['Authorization'] = f'Bearer {self._auth_token}'
        return headers
    
    @retry_with_backoff(max_retries=3)
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make an API request.

        Args:
            method: HTTP method.
            endpoint: API endpoint.
            **kwargs: Additional arguments for the request.

        Returns:
            Response data.

        Raises:
            requests.exceptions.RequestException: If the request fails.
        """
        if not self._base_url:
            raise ValueError("Base URL not set")

        url = f"{self._base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        headers = self._get_headers()

        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
            del kwargs['headers']

        try:
            response = self._session.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise
    
    def get(self, endpoint: str, **kwargs) -> Union[Dict[str, Any], list]:
        """Make a GET request.

        Args:
            endpoint: API endpoint.
            **kwargs: Additional arguments for the request.

        Returns:
            Response data.
        """
        return self._request('GET', endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a POST request.

        Args:
            endpoint: API endpoint.
            **kwargs: Additional arguments for the request.

        Returns:
            Response data.
        """
        return self._request('POST', endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a PUT request.

        Args:
            endpoint: API endpoint.
            **kwargs: Additional arguments for the request.

        Returns:
            Response data.
        """
        return self._request('PUT', endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a DELETE request.

        Args:
            endpoint: API endpoint.
            **kwargs: Additional arguments for the request.

        Returns:
            Response data.
        """
        return self._request('DELETE', endpoint, **kwargs)
