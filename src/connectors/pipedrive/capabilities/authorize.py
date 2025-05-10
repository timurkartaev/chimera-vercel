import logging
import json
import os
from typing import Dict, Any, Optional
from ..integration_connector.capabilities.authorize import AuthorizeCapability

logger = logging.getLogger(__name__)

class PipedriveAuthorizeCapability(AuthorizeCapability):
    """
    Pipedrive authorize capability that extends the base authorize capability.
    Currently uses all base functionality without modifications.
    """
    pass

class AuthorizeCapability:
    """
    Implements the Authorize capability which handles authentication
    with the external system.
    """
    
    def __init__(self, config, api_client):
        """
        Initialize the Authorize capability.
        
        Args:
            config (dict): The integration configuration
            api_client (ApiClient): The API client instance
        """
        self.config = config
        self._api_client = api_client
        
        # Set up auth configuration
        self.auth_config = self.config.get('authentication', {})
        self.auth_method = self.auth_config.get('auth_method')
        
        # Storage path for auth state
        self.auth_state_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.auth_state.json')
    
    def configure(self, config: Dict[str, Any]):
        """
        Configure the authentication settings.
        
        Args:
            config (dict): Authentication configuration
            
        Raises:
            ValueError: If the auth method is invalid or required configuration is missing
        """
        auth_method = config.get('auth_method')
        if not auth_method:
            raise ValueError("Missing auth_method in configuration")
            
        if auth_method not in ['oauth2', 'credentials']:
            raise ValueError(f"Invalid auth method: {auth_method}")
            
        if auth_method == 'oauth2' and not config.get('oauth2'):
            raise ValueError("Missing oauth2 configuration")
            
        self.auth_method = auth_method
        self.auth_config = config
    
    def get_authentication_state(self) -> Dict[str, Any]:
        """
        Get the current authentication state.
        
        Returns:
            dict: Authentication state information
        """
        try:
            if os.path.exists(self.auth_state_path):
                with open(self.auth_state_path, 'r') as f:
                    return json.load(f)
            else:
                return {"status": "disconnected"}
        except Exception as e:
            logger.error(f"Error retrieving authentication state: {str(e)}")
            return {"status": "error", "error": str(e)}
    
    def _save_authentication_state(self, state: Dict[str, Any]):
        """
        Save the authentication state.
        
        Args:
            state (dict): Authentication state to save
        """
        try:
            with open(self.auth_state_path, 'w') as f:
                json.dump(state, f)
        except Exception as e:
            logger.error(f"Error saving authentication state: {str(e)}")
    
    def authorize(self, credentials: Dict[str, Any]) -> Dict[str, Any]:
        """
        Authorize with the external system using provided credentials.
        
        Args:
            credentials (dict): The credentials provided by the user
        
        Returns:
            dict: Authorization result with status
        """
        if self.auth_method == "credentials":
            return self._authorize_credentials(credentials)
        elif self.auth_method == "oauth2":
            return self._authorize_oauth2(credentials)
        else:
            return {"status": "error", "error": f"Unsupported auth method: {self.auth_method}"}
    
    def _authorize_credentials(self, credentials: Dict[str, Any]) -> Dict[str, Any]:
        """
        Authorize using credentials-based authentication.
        
        Args:
            credentials (dict): The credentials provided by the user
        
        Returns:
            dict: Authorization result with status
        """
        # Validate required credentials
        auth_params = self.auth_config.get('auth_params', [])
        required_params = [param['id'] for param in auth_params if param.get('required', False)]
        
        for param in required_params:
            if param not in credentials or not credentials[param]:
                return {"status": "error", "error": f"Missing required credential: {param}"}
        
        try:
            # Call the API client to authenticate
            auth_response = self._api_client.post(
                'auth/login',
                json=credentials
            )
            
            if not auth_response.get('success'):
                return {"status": "error", "error": auth_response.get('error', 'Authentication failed')}
            
            # Extract token
            token = auth_response.get('token')
            
            # Update API client with the new token
            self._api_client.set_auth_token(token)
            
            # Save the authentication state
            auth_state = {
                "status": "connected",
                "metadata": {
                    "user_id": auth_response.get('user_id'),
                    "company_id": auth_response.get('company_id')
                }
            }
            self._save_authentication_state(auth_state)
            
            return auth_state
            
        except Exception as e:
            logger.error(f"Authentication error: {str(e)}")
            return {"status": "error", "error": str(e)}
    
    def _authorize_oauth2(self, credentials: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process OAuth2 authorization callback.
        
        Args:
            credentials (dict): Contains 'code' and other OAuth parameters
        
        Returns:
            dict: Authorization result with status
        """
        try:
            code = credentials.get('code')
            if not code:
                return {"status": "error", "error": "Missing authorization code"}
            
            # OAuth2 configuration
            oauth2_config = self.auth_config.get('oauth2', {})
            client_id = oauth2_config.get('client_id')
            client_secret = oauth2_config.get('client_secret')
            token_uri = oauth2_config.get('token_uri')
            redirect_uri = oauth2_config.get('redirect_uri')
            
            # Exchange the code for tokens
            token_response = self._api_client.post(
                token_uri,
                data={
                    'grant_type': 'authorization_code',
                    'code': code,
                    'client_id': client_id,
                    'client_secret': client_secret,
                    'redirect_uri': redirect_uri
                },
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            
            access_token = token_response.get('access_token')
            refresh_token = token_response.get('refresh_token')
            
            if not access_token:
                return {"status": "error", "error": "Failed to obtain access token"}
            
            # Update API client with the new tokens
            self._api_client.set_auth_token(access_token)
            if refresh_token:
                self._api_client.set_refresh_token(refresh_token)
            
            # Save the authentication state
            auth_state = {
                "status": "connected",
                "metadata": {
                    "user_id": token_response.get('user_id'),
                    "company_id": token_response.get('company_id')
                }
            }
            self._save_authentication_state(auth_state)
            
            return auth_state
            
        except Exception as e:
            logger.error(f"OAuth2 authorization error: {str(e)}")
            return {"status": "error", "error": str(e)}
    
    def refresh_token(self) -> Dict[str, Any]:
        """
        Refresh the authentication token using the refresh token.
        
        Returns:
            dict: New token data
            
        Raises:
            ValueError: If no refresh token is available
            Exception: If token refresh fails
        """
        if not self._api_client.refresh_token:
            raise ValueError("No refresh token available")
        
        try:
            # OAuth2 configuration
            oauth2_config = self.auth_config.get('oauth2', {})
            token_uri = oauth2_config.get('token_uri')
            
            response = self._api_client.post(
                token_uri,
                data={
                    'grant_type': 'refresh_token',
                    'refresh_token': self._api_client.refresh_token
                },
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                timeout=30
            )
            
            access_token = response.get('access_token')
            refresh_token = response.get('refresh_token')
            
            if not access_token:
                raise ValueError("Failed to obtain access token")
            
            # Update API client with the new tokens
            self._api_client.set_auth_token(access_token)
            if refresh_token:
                self._api_client.set_refresh_token(refresh_token)
            
            # Update authentication state
            auth_state = self.get_authentication_state()
            auth_state['status'] = 'connected'
            self._save_authentication_state(auth_state)
            
            return {
                'status': 'success',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            
        except Exception as e:
            logger.error(f"Failed to refresh token: {str(e)}")
            # Clear tokens to force re-authorization
            self._api_client.set_auth_token(None)
            self._api_client.set_refresh_token(None)
            
            # Update authentication state
            auth_state = self.get_authentication_state()
            auth_state['status'] = 'disconnected'
            self._save_authentication_state(auth_state)
            
            raise