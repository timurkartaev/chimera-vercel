import unittest
import os
import sys
import json
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector import IntegrationConnector
from chimera.integration_connector.api.client import ApiClient

@pytest.fixture
def mock_config():
    return {
        'info': {
            'name': 'Test Connector',
            'logo': 'https://example.com/logo.png',
            'categories': ['Test'],
            'website': 'https://example.com',
            'support_email': 'test@example.com',
            'version': '1.0.0',
            'developer': 'Test Developer'
        },
        'authentication': {
            'auth_method': 'oauth2',
            'oauth2': {
                'client_id': 'test-client',
                'client_secret': 'test-secret',
                'auth_uri': 'https://example.com/auth',
                'token_uri': 'https://example.com/token',
                'scopes': ['read', 'write']
            }
        },
        'entities': ['test_entity'],
        'actions': [
            {
                'action_id': 'test_action',
                'entities': ['test_entity']
            }
        ]
    }

@pytest.fixture
def connector(mock_config):
    with patch('chimera.integration_connector.connector.yaml.safe_load', return_value=mock_config):
        return IntegrationConnector()

class TestIntegrationConnector(unittest.TestCase):
    """Test suite for the IntegrationConnector class."""
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock config file path
        self.config_path = 'mock_config.yaml'
        
        # Create patches for external dependencies
        self.yaml_load_patcher = patch('yaml.safe_load')
        self.mock_yaml_load = self.yaml_load_patcher.start()
        
        # Set up a mock configuration
        self.mock_config = {
            'info': {
                'logo': 'https://example.com/logo.png',
                'name': 'Test Integration',
                'categories': ['CRM', 'Sales'],
                'website': 'https://example.com',
                'support_email': 'support@example.com',
                'version': '1.0.0',
                'developer': 'Test Company'
            },
            'authentication': {
                'auth_method': 'oauth2',
                'oauth2': {
                    'client_id': 'test_client_id',
                    'client_secret': 'test_client_secret',
                    'auth_uri': 'https://example.com/oauth/authorize',
                    'token_uri': 'https://example.com/oauth/token',
                    'scopes': ['read', 'write']
                }
            },
            'entities': ['deal', 'company', 'contact'],
            'actions': [
                {
                    'action_id': 'update',
                    'entities': ['deal', 'company', 'contact']
                },
                {
                    'action_id': 'attach_document',
                    'entities': ['deal', 'company']
                },
                {
                    'action_id': 'add_history',
                    'entities': ['deal']
                }
            ]
        }
        
        self.mock_yaml_load.return_value = self.mock_config
        
        # Mock file operations
        self.open_patcher = patch('builtins.open', unittest.mock.mock_open())
        self.mock_open = self.open_patcher.start()
        
        # Create an instance of the connector
        self.connector = IntegrationConnector(config_path=self.config_path)
        
        # Mock the API client
        self.connector._api_client = MagicMock(spec=ApiClient)
    
    def tearDown(self):
        """Tear down test fixtures after each test method is run."""
        self.yaml_load_patcher.stop()
        self.open_patcher.stop()
    
    def test_get_info(self):
        """Test that get_info returns the correct information."""
        info = self.connector.get_info()
        
        self.assertEqual(info['name'], 'Test Integration')
        self.assertEqual(info['logo'], 'https://example.com/logo.png')
        self.assertEqual(info['categories'], ['CRM', 'Sales'])
        self.assertEqual(info['website'], 'https://example.com')
        self.assertEqual(info['support_email'], 'support@example.com')
        self.assertEqual(info['version'], '1.0.0')
        self.assertEqual(info['developer'], 'Test Company')
    
    def test_get_entities(self):
        """Test that get_entities returns the correct entities."""
        entities = self.connector.get_entities()
        
        # The entities should be transformed from strings to objects with entity_type
        self.assertEqual(len(entities), 3)
        self.assertEqual(entities[0]['entity_type'], 'deal')
        self.assertEqual(entities[1]['entity_type'], 'company')
        self.assertEqual(entities[2]['entity_type'], 'contact')
    
    def test_get_actions(self):
        """Test that get_actions returns the correct actions."""
        actions = self.connector.get_actions()
        
        self.assertEqual(len(actions), 3)
        self.assertEqual(actions[0]['action_id'], 'update')
        self.assertEqual(actions[0]['entities'], ['deal', 'company', 'contact'])
        self.assertEqual(actions[1]['action_id'], 'attach_document')
        self.assertEqual(actions[1]['entities'], ['deal', 'company'])
        self.assertEqual(actions[2]['action_id'], 'add_history')
        self.assertEqual(actions[2]['entities'], ['deal'])
    
    def test_get_actions_filtered(self):
        """Test that get_actions with entity_type filter returns the correct actions."""
        actions = self.connector.get_actions(entity_type='deal')
        
        self.assertEqual(len(actions), 3)  # All actions support 'deal'
        
        actions = self.connector.get_actions(entity_type='contact')
        
        self.assertEqual(len(actions), 1)  # Only 'update' supports 'contact'
        self.assertEqual(actions[0]['action_id'], 'update')
    
    @patch('integration_connector.capabilities.authorize.AuthorizeCapability.authorize')
    def test_authorize(self, mock_authorize):
        """Test that authorize delegates to the AuthorizeCapability."""
        mock_authorize.return_value = {"status": "connected", "metadata": {"user_id": "123"}}
        
        credentials = {"username": "test", "password": "test123"}
        result = self.connector.authorize(credentials)
        
        mock_authorize.assert_called_once_with(credentials)
        self.assertEqual(result["status"], "connected")
        self.assertEqual(result["metadata"]["user_id"], "123")
    
    @patch('integration_connector.capabilities.entity.EntityCapability.get_entity_schema')
    def test_get_entity_schema(self, mock_get_entity_schema):
        """Test that get_entity_schema delegates to the EntityCapability."""
        mock_schema = {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "title": "ID"
                },
                "name": {
                    "type": "string",
                    "title": "Deal Name"
                }
            }
        }
        mock_get_entity_schema.return_value = mock_schema
        
        schema = self.connector.get_entity_schema("deal")
        
        mock_get_entity_schema.assert_called_once_with("deal", None)
        self.assertEqual(schema, mock_schema)
    
    @patch('integration_connector.capabilities.object.ObjectCapability.get_objects')
    def test_get_objects(self, mock_get_objects):
        """Test that get_objects delegates to the ObjectCapability."""
        mock_objects = [
            {"id": "deal1", "name": "Test Deal 1"},
            {"id": "deal2", "name": "Test Deal 2"}
        ]
        mock_get_objects.return_value = mock_objects
        
        objects = self.connector.get_objects("deal")
        
        mock_get_objects.assert_called_once_with("deal", None)
        self.assertEqual(objects, mock_objects)
    
    @patch('integration_connector.capabilities.object.ObjectCapability.get_object_data')
    def test_get_object_data(self, mock_get_object_data):
        """Test that get_object_data delegates to the ObjectCapability."""
        mock_data = {
            "id": "deal1",
            "name": "Test Deal",
            "amount": 1000,
            "stage": "Proposal"
        }
        mock_get_object_data.return_value = mock_data
        
        data = self.connector.get_object_data("deal", None, "deal1")
        
        mock_get_object_data.assert_called_once_with("deal", None, "deal1")
        self.assertEqual(data, mock_data)
    
    @patch('integration_connector.capabilities.action.ActionCapability.execute_action')
    def test_execute_action(self, mock_execute_action):
        """Test that execute_action delegates to the ActionCapability."""
        mock_result = {
            "success": True,
            "object_id": "deal1",
            "updated_properties": ["name", "amount"]
        }
        mock_execute_action.return_value = mock_result
        
        params = {"properties": {"name": "Updated Deal", "amount": 2000}}
        result = self.connector.execute_action("update", "deal", "deal1", params)
        
        mock_execute_action.assert_called_once_with("update", "deal", "deal1", params)
        self.assertEqual(result, mock_result)

def test_get_info(connector, mock_config):
    """Test getting connector info."""
    info = connector.get_info()
    assert info['name'] == mock_config['info']['name']
    assert info['logo'] == mock_config['info']['logo']
    assert info['categories'] == mock_config['info']['categories']

def test_get_entities(connector, mock_config):
    """Test getting available entities."""
    entities = connector.get_entities()
    assert entities == mock_config['entities']

def test_get_actions(connector, mock_config):
    """Test getting available actions."""
    actions = connector.get_actions()
    assert len(actions) == len(mock_config['actions'])
    assert actions[0]['action_id'] == mock_config['actions'][0]['action_id']

def test_authorize(connector):
    """Test authorization."""
    credentials = {'code': 'test-code'}
    result = connector.authorize(credentials)
    assert result is not None  # Add more specific assertions based on your implementation

if __name__ == '__main__':
    unittest.main()