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
    
    def _refresh_auth_token(self):
        """
        Refresh the authentication token using the refresh token.
        
        Raises:
            Exception: If token refresh fails
        """
        if not self.refresh_token:
            raise ValueError("No refresh token available")
        
        # Implementation will depend on the specific API
        # This is just an example
        try:
            response = requests.post(
                f"{self._base_url}/oauth/token",
                json={
                    'grant_type': 'refresh_token',
                    'refresh_token': self.refresh_token
                },
                headers={'Content-Type': 'application/json'},
                timeout=30
            )
            
            response.raise_for_status()
            token_data = response.json()
            
            self.set_auth_token(token_data.get('access_token'))
            
        except Exception as e:
            logger.error(f"Failed to refresh token: {str(e)}")
            # Clear tokens to force re-authorization
            self._auth_token = None
            self.refresh_token = None
            self._get_headers().pop('Authorization', None)
            raise
    
    # Example API methods for specific endpoints
    # These would be customized based on the external system's API
    
    def authenticate(self, credentials):
        """
        Authenticate with the external system.
        
        Args:
            credentials (dict): Authentication credentials
        
        Returns:
            dict: Authentication response
        """
        # Implementation depends on the specific API
        pass
    
    def get_deals(self):
        """
        Get all deals from the external system.
        
        Returns:
            dict: Deals data
        """
        return self.get('deals')
    
    def get_deal(self, deal_id):
        """
        Get a specific deal from the external system.
        
        Args:
            deal_id (str): The ID of the deal
        
        Returns:
            dict: Deal data
        """
        return self.get(f'deals/{deal_id}')
    
    def update_deal(self, deal_id, properties):
        """
        Update a deal in the external system.
        
        Args:
            deal_id (str): The ID of the deal
            properties (dict): Properties to update
        
        Returns:
            dict: Updated deal data
        """
        return self.put(f'deals/{deal_id}', data=properties)
    
    def get_companies(self):
        """
        Get all companies from the external system.
        
        Returns:
            dict: Companies data
        """
        return self.get('companies')
    
    def get_company(self, company_id):
        """
        Get a specific company from the external system.
        
        Args:
            company_id (str): The ID of the company
        
        Returns:
            dict: Company data
        """
        return self.get(f'companies/{company_id}')
    
    def update_company(self, company_id, properties):
        """
        Update a company in the external system.
        
        Args:
            company_id (str): The ID of the company
            properties (dict): Properties to update
        
        Returns:
            dict: Updated company data
        """
        return self.put(f'companies/{company_id}', data=properties)
    
    def get_contacts(self):
        """
        Get all contacts from the external system.
        
        Returns:
            dict: Contacts data
        """
        return self.get('contacts')
    
    def get_contact(self, contact_id):
        """
        Get a specific contact from the external system.
        
        Args:
            contact_id (str): The ID of the contact
        
        Returns:
            dict: Contact data
        """
        return self.get(f'contacts/{contact_id}')
    
    def update_contact(self, contact_id, properties):
        """
        Update a contact in the external system.
        
        Args:
            contact_id (str): The ID of the contact
            properties (dict): Properties to update
        
        Returns:
            dict: Updated contact data
        """
        return self.put(f'contacts/{contact_id}', data=properties)
    
    def get_custom_objects(self, entity_id):
        """
        Get all instances of a custom object type.
        
        Args:
            entity_id (str): The ID of the custom object type
        
        Returns:
            dict: Custom objects data
        """
        return self.get(f'custom_objects/{entity_id}')
    
    def get_custom_object(self, entity_id, object_id):
        """
        Get a specific custom object instance.
        
        Args:
            entity_id (str): The ID of the custom object type
            object_id (str): The ID of the custom object instance
        
        Returns:
            dict: Custom object data
        """
        return self.get(f'custom_objects/{entity_id}/{object_id}')
    
    def attach_document(self, entity_type, object_id, document_id, document_name, document_url):
        """
        Attach a document to an object in the external system.
        
        Args:
            entity_type (str): The type of entity
            object_id (str): The ID of the object
            document_id (str): The ID of the document
            document_name (str): The name of the document
            document_url (str): The URL of the document
        
        Returns:
            dict: Result of the attachment operation
        """
        data = {
            'document_id': document_id,
            'document_name': document_name,
            'document_url': document_url
        }
        return self.post(f'{entity_type}/{object_id}/documents', data=data)
    
    def add_deal_activity(self, deal_id, activity_type, document_id, document_name, message):
        """
        Add an activity to a deal's history.
        
        Args:
            deal_id (str): The ID of the deal
            activity_type (str): The type of activity
            document_id (str): The ID of the related document
            document_name (str): The name of the document
            message (str): Activity message
        
        Returns:
            dict: Result of the activity creation
        """
        data = {
            'activity_type': activity_type,
            'document_id': document_id,
            'document_name': document_name,
            'message': message
        }
        return self.post(f'deals/{deal_id}/activities', data=data)

    def refresh_auth_token(self, refresh_token: str, token_url: str) -> Dict[str, str]:
        """Refresh the authentication token.

        Args:
            refresh_token: Refresh token.
            token_url: Token endpoint URL.

        Returns:
            Dictionary containing the new access token and refresh token.
        """
        response = self.post(token_url, data={'grant_type': 'refresh_token', 'refresh_token': refresh_token})
        self._auth_token = response.get('access_token')
        return response