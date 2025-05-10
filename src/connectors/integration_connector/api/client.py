import logging
import requests
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class ApiClient:
    """Base API client for making HTTP requests to external systems."""
    
    def __init__(self, base_url: Optional[str] = None):
        """
        Initialize the API client.
        
        Args:
            base_url (str, optional): Base URL for API requests
        """
        self.base_url = base_url
        self.session = requests.Session()
        self._auth_token = None
        self._refresh_token = None
    
    def set_auth_token(self, token: Optional[str]):
        """Set the authentication token."""
        self._auth_token = token
        if token:
            self.session.headers.update({'Authorization': f'Bearer {token}'})
        else:
            self.session.headers.pop('Authorization', None)
    
    def set_refresh_token(self, token: Optional[str]):
        """Set the refresh token."""
        self._refresh_token = token
    
    def get(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a GET request."""
        url = f"{self.base_url}/{endpoint}" if self.base_url else endpoint
        response = self.session.get(url, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a POST request."""
        url = f"{self.base_url}/{endpoint}" if self.base_url else endpoint
        response = self.session.post(url, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a PUT request."""
        url = f"{self.base_url}/{endpoint}" if self.base_url else endpoint
        response = self.session.put(url, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make a DELETE request."""
        url = f"{self.base_url}/{endpoint}" if self.base_url else endpoint
        response = self.session.delete(url, **kwargs)
        response.raise_for_status()
        return response.json() 