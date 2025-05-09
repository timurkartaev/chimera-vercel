import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest
import requests

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.api.client import ApiClient

def test_api_client_initialization():
    """Test API client initialization."""
    client = ApiClient()
    assert client._base_url is None
    assert client._auth_token is None

def test_set_base_url():
    """Test setting base URL."""
    client = ApiClient()
    base_url = "https://api.example.com"
    client.set_base_url(base_url)
    assert client._base_url == base_url

def test_set_auth_token():
    """Test setting auth token."""
    client = ApiClient()
    token = "test-token"
    client.set_auth_token(token)
    assert client._auth_token == token

def test_get_headers():
    """Test getting headers."""
    client = ApiClient()
    client.set_auth_token("test-token")
    headers = client._get_headers()
    assert headers["Content-Type"] == "application/json"
    assert headers["Accept"] == "application/json"
    assert headers["Authorization"] == "Bearer test-token"

@patch("requests.Session.get")
def test_get_request(mock_get):
    """Test making GET request."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": "test"}
    mock_get.return_value = mock_response
    
    client = ApiClient()
    client.set_base_url("https://api.example.com")
    result = client.get("test")
    
    assert result == {"data": "test"}
    mock_get.assert_called_once()

@patch("requests.Session.post")
def test_post_request(mock_post):
    """Test making POST request."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": "test"}
    mock_post.return_value = mock_response
    
    client = ApiClient()
    client.set_base_url("https://api.example.com")
    result = client.post("test", {"key": "value"})
    
    assert result == {"data": "test"}
    mock_post.assert_called_once()

@patch("requests.Session.put")
def test_put_request(mock_put):
    """Test making PUT request."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": "test"}
    mock_put.return_value = mock_response
    
    client = ApiClient()
    client.set_base_url("https://api.example.com")
    result = client.put("test", {"key": "value"})
    
    assert result == {"data": "test"}
    mock_put.assert_called_once()

@patch("requests.Session.delete")
def test_delete_request(mock_delete):
    """Test making DELETE request."""
    mock_response = MagicMock()
    mock_delete.return_value = mock_response
    
    client = ApiClient()
    client.set_base_url("https://api.example.com")
    client.delete("test")
    
    mock_delete.assert_called_once()

class TestApiClient(unittest.TestCase):
    """Test suite for the ApiClient class."""
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        self.api_client = ApiClient()
        self.api_client.set_base_url('https://api.example.com')
    
    @patch('requests.request')
    def test_request(self, mock_request):
        """Test that _request makes a proper API request."""
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = '{"success": true, "data": [1, 2, 3]}'
        mock_response.json.return_value = {"success": True, "data": [1, 2, 3]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response
        
        # Make a request
        result = self.api_client._request('GET', 'test/endpoint', params={'param': 'value'})
        
        # Check the request
        mock_request.assert_called_once_with(
            'GET',
            'https://api.example.com/test/endpoint',
            json=None,
            params={'param': 'value'},
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
            timeout=30
        )
        
        # Check the result
        self.assertEqual(result, {"success": True, "data": [1, 2, 3]})
    
    @patch('requests.request')
    def test_request_with_auth_token(self, mock_request):
        """Test that _request includes the auth token in headers."""
        # Set auth token
        self.api_client.set_auth_token('test_token')
        
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = '{}'
        mock_response.json.return_value = {}
        mock_response.status_code = 200
        mock_request.return_value = mock_response
        
        # Make a request
        self.api_client._request('GET', 'test/endpoint')
        
        # Check the request
        mock_request.assert_called_once_with(
            'GET',
            'https://api.example.com/test/endpoint',
            json=None,
            params=None,
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer test_token'
            },
            timeout=30
        )
    
    @patch('requests.request')
    def test_convenience_methods(self, mock_request):
        """Test the convenience methods (get, post, put, delete)."""
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = '{}'
        mock_response.json.return_value = {}
        mock_response.status_code = 200
        mock_request.return_value = mock_response
        
        # Test GET
        self.api_client.get('test/get', params={'param': 'value'})
        mock_request.assert_called_with(
            'GET',
            'https://api.example.com/test/get',
            json=None,
            params={'param': 'value'},
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
            timeout=30
        )
        
        # Test POST
        self.api_client.post('test/post', data={'key': 'value'})
        mock_request.assert_called_with(
            'POST',
            'https://api.example.com/test/post',
            json={'key': 'value'},
            params=None,
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
            timeout=30
        )
        
        # Test PUT
        self.api_client.put('test/put', data={'key': 'value'})
        mock_request.assert_called_with(
            'PUT',
            'https://api.example.com/test/put',
            json={'key': 'value'},
            params=None,
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
            timeout=30
        )
        
        # Test DELETE
        self.api_client.delete('test/delete')
        mock_request.assert_called_with(
            'DELETE',
            'https://api.example.com/test/delete',
            json=None,
            params=None,
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
            timeout=30
        )
    
    @patch('requests.post')
    def test_refresh_auth_token(self, mock_post):
        """Test that _refresh_auth_token refreshes the token."""
        # Set up the refresh token
        self.api_client.refresh_token = 'test_refresh_token'
        
        # Mock the response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'access_token': 'new_access_token',
            'refresh_token': 'new_refresh_token'
        }
        mock_post.return_value = mock_response
        
        # Call the method
        self.api_client._refresh_auth_token()
        
        # Check the request
        mock_post.assert_called_once_with(
            'https://api.example.com/oauth/token',
            json={
                'grant_type': 'refresh_token',
                'refresh_token': 'test_refresh_token'
            },
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        
        # Check that the tokens were updated
        self.assertEqual(self.api_client.auth_token, 'new_access_token')
        self.assertEqual(self.api_client.refresh_token, 'new_refresh_token')
        self.assertEqual(self.api_client.headers['Authorization'], 'Bearer new_access_token')
    
    def test_no_base_url(self):
        """Test that _request raises an error when base_url is not set."""
        # Create a new client without setting base_url
        client = ApiClient()
        
        # Try to make a request
        with self.assertRaises(ValueError):
            client._request('GET', 'test/endpoint')

if __name__ == '__main__':
    unittest.main()