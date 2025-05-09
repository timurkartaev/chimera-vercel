import logging
import json
import os

logger = logging.getLogger(__name__)

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
        
        # Storage path for auth state (would be replaced with your platform's storage mechanism)
        self.auth_state_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.auth_state.json')
    
    def get_authentication_state(self):
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
    
    def _save_authentication_state(self, state):
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
    
    def authorize(self, credentials):
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
    
    def _authorize_credentials(self, credentials):
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
            # Call the API client to authenticate with the external system
            # This implementation depends on the specific API
            auth_response = self._api_client.authenticate(credentials)
            
            if not auth_response.get('success'):
                return {"status": "error", "error": auth_response.get('error', 'Authentication failed')}
            
            # Extract tokens or session information
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
    
    def _authorize_oauth2(self, credentials):
        """
        Process OAuth2 authorization callback.
        
        This method handles the OAuth2 authorization code exchange.
        
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
            
            # In a real implementation, you would make a request to the token_uri
            # to exchange the code for tokens. This is simplified.
            
            # Call the API client to exchange the code for tokens
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
            self._api_client.set_auth_token(access_token, refresh_token)
            
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