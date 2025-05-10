import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.capabilities.authorize import AuthorizeCapability
from chimera.integration_connector.api.client import ApiClient

@pytest.fixture
def mock_config():
    return {
        'authentication': {
            'auth_method': 'oauth2',
            'oauth2': {
                'client_id': 'test-client',
                'client_secret': 'test-secret',
                'auth_uri': 'https://example.com/auth',
                'token_uri': 'https://example.com/token',
                'scopes': ['read', 'write']
            }
        }
    }

@pytest.fixture
def mock_api_client():
    return MagicMock(spec=ApiClient)

def test_authorize_capability_initialization(mock_config, mock_api_client):
    """Test authorize capability initialization."""
    capability = AuthorizeCapability(mock_config, mock_api_client)
    assert capability.auth_config == mock_config['authentication']
    assert capability.auth_method == 'oauth2'

def test_configure_oauth2(mock_config, mock_api_client):
    """Test configuring OAuth2 authentication."""
    capability = AuthorizeCapability(mock_config, mock_api_client)
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
    assert capability.auth_config['oauth2'] == config['oauth2']

@patch('requests.post')
def test_oauth2_token_exchange(mock_post, mock_config, mock_api_client):
    """Test OAuth2 token exchange."""
    # Set up the mock API client response
    mock_api_client.post.return_value = {
        'access_token': 'test-token',
        'refresh_token': 'test-refresh',
        'expires_in': 3600,
        'user_id': 'test-user',
        'company_id': 'test-company'
    }
    
    capability = AuthorizeCapability(mock_config, mock_api_client)
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
    
    assert result['status'] == 'connected'
    assert result['metadata']['user_id'] == 'test-user'
    assert result['metadata']['company_id'] == 'test-company'
    mock_api_client.set_auth_token.assert_called_once_with('test-token')
    mock_api_client.set_refresh_token.assert_called_once_with('test-refresh')

def test_invalid_auth_method(mock_config, mock_api_client):
    """Test configuring invalid authentication method."""
    capability = AuthorizeCapability(mock_config, mock_api_client)
    config = {
        'auth_method': 'invalid',
        'invalid': {}
    }
    with pytest.raises(ValueError):
        capability.configure(config)

def test_missing_oauth2_config(mock_config, mock_api_client):
    """Test missing OAuth2 configuration."""
    capability = AuthorizeCapability(mock_config, mock_api_client)
    config = {
        'auth_method': 'oauth2'
    }
    with pytest.raises(ValueError):
        capability.configure(config)

if __name__ == '__main__':
    unittest.main()