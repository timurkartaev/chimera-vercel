import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.capabilities.info import InfoCapability
from chimera.integration_connector.api.client import ApiClient

@pytest.fixture
def mock_config():
    return {
        'info': {
            'name': 'Test Integration',
            'logo': 'https://example.com/logo.png',
            'categories': ['Test'],
            'website': 'https://example.com',
            'support_email': 'test@example.com',
            'version': '1.0.0',
            'developer': 'Test Developer'
        }
    }

@pytest.fixture
def mock_api_client():
    return MagicMock(spec=ApiClient)

def test_info_capability_initialization(mock_config, mock_api_client):
    """Test info capability initialization."""
    capability = InfoCapability(mock_config, mock_api_client)
    assert capability.info == {}

def test_configure_info(mock_config, mock_api_client):
    """Test configuring info."""
    capability = InfoCapability(mock_config, mock_api_client)
    info = {
        'name': 'Test Integration',
        'logo': 'https://example.com/logo.png',
        'categories': ['Test'],
        'website': 'https://example.com',
        'support_email': 'test@example.com',
        'version': '1.0.0',
        'developer': 'Test Developer'
    }
    capability.configure(info)
    assert capability.info == info

def test_get_info(mock_config, mock_api_client):
    """Test getting info."""
    capability = InfoCapability(mock_config, mock_api_client)
    info = {
        'name': 'Test Integration',
        'logo': 'https://example.com/logo.png',
        'categories': ['Test'],
        'website': 'https://example.com',
        'support_email': 'test@example.com',
        'version': '1.0.0',
        'developer': 'Test Developer'
    }
    capability.configure(info)
    result = capability.get_info()
    assert result == info

def test_missing_required_fields(mock_config, mock_api_client):
    """Test configuring info with missing required fields."""
    capability = InfoCapability(mock_config, mock_api_client)
    info = {
        'name': 'Test Integration'
        # Missing other required fields
    }
    with pytest.raises(ValueError):
        capability.configure(info)

class TestInfoCapability(unittest.TestCase):
    """Test suite for the InfoCapability class."""
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock config
        self.config = {
            'info': {
                'logo': 'https://example.com/logo.png',
                'name': 'Test Integration',
                'categories': ['CRM', 'Sales'],
                'website': 'https://example.com',
                'support_email': 'support@example.com',
                'version': '1.0.0',
                'developer': 'Test Company'
            }
        }
        
        # Create a mock API client
        self.api_client = MagicMock(spec=ApiClient)
        
        # Create an instance of the capability
        self.info_capability = InfoCapability(self.config, self.api_client)
    
    def test_get_info(self):
        """Test that get_info returns the correct information."""
        info = self.info_capability.get_info()
        
        self.assertEqual(info['name'], 'Test Integration')
        self.assertEqual(info['logo'], 'https://example.com/logo.png')
        self.assertEqual(info['categories'], ['CRM', 'Sales'])
        self.assertEqual(info['website'], 'https://example.com')
        self.assertEqual(info['support_email'], 'support@example.com')
        self.assertEqual(info['version'], '1.0.0')
        self.assertEqual(info['developer'], 'Test Company')
    
    def test_get_info_missing_required_field(self):
        """Test that get_info raises an error for missing required fields."""
        # Create a config with missing required fields
        config_missing_fields = {
            'info': {
                # Missing 'logo'
                'name': 'Test Integration'
            }
        }
        
        # Create an instance with the incomplete config
        info_capability = InfoCapability(config_missing_fields, self.api_client)
        
        # Check that it raises a ValueError
        with self.assertRaises(ValueError):
            info_capability.get_info()
    
    def test_get_info_missing_optional_field(self):
        """Test that get_info handles missing optional fields."""
        # Create a config with only required fields
        config_minimal = {
            'info': {
                'logo': 'https://example.com/logo.png',
                'name': 'Test Integration'
            }
        }
        
        # Create an instance with the minimal config
        info_capability = InfoCapability(config_minimal, self.api_client)
        
        # Get info
        info = info_capability.get_info()
        
        # Check required fields
        self.assertEqual(info['name'], 'Test Integration')
        self.assertEqual(info['logo'], 'https://example.com/logo.png')
        
        # Check optional fields have defaults
        self.assertEqual(info['categories'], [])
        self.assertIsNone(info['website'])
        self.assertIsNone(info['support_email'])
        self.assertIsNone(info['version'])
        self.assertIsNone(info['developer'])

if __name__ == '__main__':
    unittest.main()