import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.capabilities.authorize import AuthorizeCapability

def test_authorize_capability_initialization():
    """Test authorize capability initialization."""
    capability = AuthorizeCapability()
    assert capability.auth_config is None
    assert capability.auth_method is None

def test_configure_oauth2():
    """Test configuring OAuth2 authentication."""
    capability = AuthorizeCapability()
    config = {
        'auth_method': 'oauth2',
        'oauth2': {
            'client_id': 'test-client',
            'client_secret': 'test-secret',
            'auth_uri': 'https://example.com/auth',
            'token_uri': 'https://example.com/token',
            'scopes': ['read', 'write']
        }
    }
    capability.configure(config)
    assert capability.auth_method == 'oauth2'
    assert capability.auth_config == config['oauth2']

@patch('requests.post')
def test_oauth2_token_exchange(mock_post):
    """Test OAuth2 token exchange."""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'access_token': 'test-token',
        'refresh_token': 'test-refresh',
        'expires_in': 3600
    }
    mock_post.return_value = mock_response
    
    capability = AuthorizeCapability()
    config = {
        'auth_method': 'oauth2',
        'oauth2': {
            'client_id': 'test-client',
            'client_secret': 'test-secret',
            'auth_uri': 'https://example.com/auth',
            'token_uri': 'https://example.com/token',
            'scopes': ['read', 'write']
        }
    }
    capability.configure(config)
    
    credentials = {'code': 'test-code'}
    result = capability.authorize(credentials)
    
    assert result['access_token'] == 'test-token'
    assert result['refresh_token'] == 'test-refresh'
    mock_post.assert_called_once()

def test_invalid_auth_method():
    """Test configuring invalid authentication method."""
    capability = AuthorizeCapability()
    config = {
        'auth_method': 'invalid',
        'invalid': {}
    }
    with pytest.raises(ValueError):
        capability.configure(config)

def test_missing_oauth2_config():
    """Test missing OAuth2 configuration."""
    capability = AuthorizeCapability()
    config = {
        'auth_method': 'oauth2'
    }
    with pytest.raises(ValueError):
        capability.configure(config)

if __name__ == '__main__':
    unittest.main()