import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.capabilities.action import ActionCapability
from chimera.integration_connector.api.client import ApiClient

@pytest.fixture
def mock_config():
    return {
        'actions': [
            {
                'action_id': 'test_action',
                'entities': ['test_entity'],
                'parameters': {
                    'param1': {'type': 'string'}
                }
            }
        ]
    }

@pytest.fixture
def mock_api_client():
    return MagicMock(spec=ApiClient)

def test_action_capability_initialization(mock_config, mock_api_client):
    """Test action capability initialization."""
    capability = ActionCapability(mock_config, mock_api_client)
    assert capability.actions == []

def test_register_action(mock_config, mock_api_client):
    """Test registering an action."""
    capability = ActionCapability(mock_config, mock_api_client)
    action = {
        'action_id': 'test_action',
        'entities': ['test_entity'],
        'parameters': {
            'param1': {'type': 'string'}
        }
    }
    capability.register_action(action)
    assert len(capability.actions) == 1
    assert capability.actions[0] == action

def test_get_actions(mock_config, mock_api_client):
    """Test getting all actions."""
    capability = ActionCapability(mock_config, mock_api_client)
    action1 = {'action_id': 'action1', 'entities': ['entity1']}
    action2 = {'action_id': 'action2', 'entities': ['entity2']}
    capability.register_action(action1)
    capability.register_action(action2)
    
    actions = capability.get_actions()
    assert len(actions) == 2
    assert action1 in actions
    assert action2 in actions

def test_get_actions_filtered(mock_config, mock_api_client):
    """Test getting actions filtered by entity type."""
    capability = ActionCapability(mock_config, mock_api_client)
    action1 = {'action_id': 'action1', 'entities': ['entity1', 'entity2']}
    action2 = {'action_id': 'action2', 'entities': ['entity2']}
    capability.register_action(action1)
    capability.register_action(action2)
    
    actions = capability.get_actions(entity_type='entity1')
    assert len(actions) == 1
    assert actions[0] == action1

def test_execute_action(mock_config, mock_api_client):
    """Test executing an action."""
    capability = ActionCapability(mock_config, mock_api_client)
    action = {
        'action_id': 'test_action',
        'entities': ['test_entity'],
        'handler': lambda params: {'result': 'success'}
    }
    capability.register_action(action)
    
    result = capability.execute_action('test_action', 'test_entity', 'object_id', {'param': 'value'})
    assert result == {'result': 'success'}

class TestActionCapability(unittest.TestCase):
    """Test suite for the ActionCapability class."""
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock config
        self.config = {
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
        
        # Create a mock API client
        self.api_client = MagicMock(spec=ApiClient)
        
        # Create an instance of the capability
        self.action_capability = ActionCapability(self.config, self.api_client)
    
    def test_get_actions(self):
        """Test that get_actions returns all actions when no entity_type is specified."""
        actions = self.action_capability.get_actions()
        
        self.assertEqual(len(actions), 3)
        self.assertEqual(actions[0]['action_id'], 'update')
        self.assertEqual(actions[0]['entities'], ['deal', 'company', 'contact'])
        self.assertEqual(actions[1]['action_id'], 'attach_document')
        self.assertEqual(actions[1]['entities'], ['deal', 'company'])
        self.assertEqual(actions[2]['action_id'], 'add_history')
        self.assertEqual(actions[2]['entities'], ['deal'])
    
    def test_get_actions_filtered(self):
        """Test that get_actions returns filtered actions when entity_type is specified."""
        # Filter by 'deal'
        actions = self.action_capability.get_actions(entity_type='deal')
        
        self.assertEqual(len(actions), 3)  # All actions support 'deal'
        
        # Filter by 'company'
        actions = self.action_capability.get_actions(entity_type='company')
        
        self.assertEqual(len(actions), 2)  # 'update' and 'attach_document' support 'company'
        self.assertEqual(actions[0]['action_id'], 'update')
        self.assertEqual(actions[1]['action_id'], 'attach_document')
        
        # Filter by 'contact'
        actions = self.action_capability.get_actions(entity_type='contact')
        
        self.assertEqual(len(actions), 1)  # Only 'update' supports 'contact'
        self.assertEqual(actions[0]['action_id'], 'update')
    
    def test_execute_action_update(self):
        """Test that execute_action for update action works correctly."""
        # Mock authentication state
        self.action_capability._get_authentication_state = MagicMock(return_value={"status": "connected"})
        
        # Mock update_deal method
        self.api_client.update_deal = MagicMock(return_value={"success": True})
        
        # Execute the action
        params = {"properties": {"name": "Updated Deal", "amount": 5000}}
        result = self.action_capability.execute_action("update", "deal", "deal123", params)
        
        # Check the result
        self.assertTrue(result["success"])
        self.assertEqual(result["object_id"], "deal123")
        self.assertEqual(set(result["updated_properties"]), {"name", "amount"})
        
        # Verify API client call
        self.api_client.update_deal.assert_called_once_with("deal123", {"name": "Updated Deal", "amount": 5000})
    
    def test_execute_action_attach_document(self):
        """Test that execute_action for attach_document action works correctly."""
        # Mock authentication state
        self.action_capability._get_authentication_state = MagicMock(return_value={"status": "connected"})
        
        # Mock attach_document method
        self.api_client.attach_document = MagicMock(return_value={"success": True})
        
        # Execute the action
        params = {
            "document_id": "doc123",
            "document_name": "Test Document",
            "document_url": "https://example.com/docs/doc123"
        }
        result = self.action_capability.execute_action("attach_document", "deal", "deal123", params)
        
        # Check the result
        self.assertTrue(result["success"])
        self.assertEqual(result["object_id"], "deal123")
        self.assertEqual(result["document_id"], "doc123")
        
        # Verify API client call
        self.api_client.attach_document.assert_called_once_with(
            "deal",
            "deal123",
            "doc123",
            "Test Document",
            "https://example.com/docs/doc123"
        )
    
    def test_execute_action_add_history(self):
        """Test that execute_action for add_history action works correctly."""
        # Mock authentication state
        self.action_capability._get_authentication_state = MagicMock(return_value={"status": "connected"})
        
        # Mock add_deal_activity method
        self.api_client.add_deal_activity = MagicMock(return_value={"success": True})
        
        # Execute the action
        params = {
            "activity_type": "document_sent",
            "document_id": "doc123",
            "document_name": "Test Document",
            "message": "Document sent to client"
        }
        result = self.action_capability.execute_action("add_history", "deal", "deal123", params)
        
        # Check the result
        self.assertTrue(result["success"])
        self.assertEqual(result["object_id"], "deal123")
        self.assertEqual(result["activity_type"], "document_sent")
        
        # Verify API client call
        self.api_client.add_deal_activity.assert_called_once_with(
            "deal123",
            "document_sent",
            "doc123",
            "Test Document",
            "Document sent to client"
        )
    
    def test_execute_action_unsupported_entity(self):
        """Test that execute_action returns an error for unsupported entity types."""
        # Mock authentication state
        self.action_capability._get_authentication_state = MagicMock(return_value={"status": "connected"})
        
        # Try to execute an action on an unsupported entity
        result = self.action_capability.execute_action("add_history", "contact", "contact123", {})
        
        # Check the result
        self.assertFalse(result["success"])
        self.assertIn("not supported for entity type", result["error"])
    
    def test_execute_action_missing_params(self):
        """Test that execute_action returns an error for missing parameters."""
        # Mock authentication state
        self.action_capability._get_authentication_state = MagicMock(return_value={"status": "connected"})
        
        # Try to execute an action without required parameters
        result = self.action_capability.execute_action("attach_document", "deal", "deal123", {})
        
        # Check the result
        self.assertFalse(result["success"])
        self.assertIn("Missing required document parameters", result["error"])
    
    def test_execute_action_not_authenticated(self):
        """Test that execute_action returns an error when not authenticated."""
        # Mock authentication state
        self.action_capability._get_authentication_state = MagicMock(return_value={"status": "disconnected"})
        
        # Try to execute an action without authentication
        result = self.action_capability.execute_action("update", "deal", "deal123", {"properties": {}})
        
        # Check the result
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "Authentication required")
    
    def test_execute_action_error_handling(self):
        """Test that execute_action handles API errors correctly."""
        # Mock authentication state
        self.action_capability._get_authentication_state = MagicMock(return_value={"status": "connected"})
        
        # Mock update_deal method to raise an exception
        self.api_client.update_deal = MagicMock(side_effect=Exception("API error"))
        
        # Execute the action
        params = {"properties": {"name": "Updated Deal"}}
        result = self.action_capability.execute_action("update", "deal", "deal123", params)
        
        # Check the result
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "API error")

if __name__ == '__main__':
    unittest.main()