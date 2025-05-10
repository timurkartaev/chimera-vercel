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
            },
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

@pytest.fixture
def mock_api_client():
    return MagicMock(spec=ApiClient)

def test_action_capability_initialization(mock_config, mock_api_client):
    """Test action capability initialization."""
    capability = ActionCapability(mock_config, mock_api_client)
    # Static actions from config are registered during initialization
    assert len(capability.actions) == 4
    assert capability.actions[0]['action_id'] == 'test_action'
    assert capability.actions[0]['entities'] == ['test_entity']
    assert capability.actions[1]['action_id'] == 'update'
    assert capability.actions[1]['entities'] == ['deal', 'company', 'contact']
    assert capability.actions[2]['action_id'] == 'attach_document'
    assert capability.actions[2]['entities'] == ['deal', 'company']
    assert capability.actions[3]['action_id'] == 'add_history'
    assert capability.actions[3]['entities'] == ['deal']

def test_register_action(mock_config, mock_api_client):
    """Test registering a new action."""
    capability = ActionCapability(mock_config, mock_api_client)
    action = {'action_id': 'test_action2', 'entities': ['test_entity']}
    capability.register_action(action)
    assert len(capability.actions) == 5
    assert action in capability.actions

def test_get_actions(mock_config, mock_api_client):
    """Test getting all actions."""
    capability = ActionCapability(mock_config, mock_api_client)
    action1 = {'action_id': 'action1', 'entities': ['entity1']}
    action2 = {'action_id': 'action2', 'entities': ['entity2']}
    capability.register_action(action1)
    capability.register_action(action2)
    
    actions = capability.get_actions()
    assert len(actions) == 6  # 4 from config + 2 registered
    assert action1 in actions
    assert action2 in actions

def test_get_actions_filtered(mock_config, mock_api_client):
    """Test getting actions filtered by entity type."""
    capability = ActionCapability(mock_config, mock_api_client)
    action1 = {'action_id': 'action1', 'entities': ['entity1', 'entity2']}
    action2 = {'action_id': 'action2', 'entities': ['entity2']}
    capability.register_action(action1)
    capability.register_action(action2)
    
    actions = capability.get_actions({"entity_type": "entity1"})
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
    # Override the existing test_action with our custom handler
    capability.register_action(action)
    
    params = {
        'action_id': 'test_action',
        'entity_type': 'test_entity',
        'object_id': 'object_id',
        'param': 'value'
    }
    result = capability.execute_action(params)
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
        actions = self.action_capability.get_actions({"entity_type": "deal"})
        
        self.assertEqual(len(actions), 3)  # All actions support 'deal'
        
        # Filter by 'company'
        actions = self.action_capability.get_actions({"entity_type": "company"})
        
        self.assertEqual(len(actions), 2)  # 'update' and 'attach_document' support 'company'
        self.assertEqual(actions[0]['action_id'], 'update')
        self.assertEqual(actions[1]['action_id'], 'attach_document')
        
        # Filter by 'contact'
        actions = self.action_capability.get_actions({"entity_type": "contact"})
        
        self.assertEqual(len(actions), 1)  # Only 'update' supports 'contact'
        self.assertEqual(actions[0]['action_id'], 'update')
    
    def test_execute_action_update(self):
        """Test that execute_action for update action works correctly."""
        # Mock update_deal method
        self.api_client.update_deal = MagicMock(return_value={"success": True})
        
        # Execute the action
        params = {
            "action_id": "update",
            "entity_type": "deal",
            "object_id": "deal123",
            "properties": {"name": "Updated Deal", "amount": 5000}
        }
        result = self.action_capability.execute_action(params)
        
        # Check the result
        self.assertTrue(result["success"])
        self.assertEqual(result["object_id"], "deal123")
        self.assertEqual(set(result["updated_properties"]), {"name", "amount"})
        
        # Verify API client call
        self.api_client.update_deal.assert_called_once_with("deal123", {"name": "Updated Deal", "amount": 5000})
    
    def test_execute_action_attach_document(self):
        """Test that execute_action for attach_document action works correctly."""
        # Mock attach_document method
        self.api_client.attach_document = MagicMock(return_value={"success": True})
        
        # Execute the action
        params = {
            "action_id": "attach_document",
            "entity_type": "deal",
            "object_id": "deal123",
            "document_id": "doc123",
            "document_name": "Test Document",
            "document_url": "https://example.com/docs/doc123"
        }
        result = self.action_capability.execute_action(params)
        
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
        # Mock add_deal_activity method
        self.api_client.add_deal_activity = MagicMock(return_value={"success": True})
        
        # Execute the action
        params = {
            "action_id": "add_history",
            "entity_type": "deal",
            "object_id": "deal123",
            "activity_type": "document_sent",
            "document_id": "doc123",
            "document_name": "Test Document",
            "message": "Document sent to client"
        }
        result = self.action_capability.execute_action(params)
        
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
        # Try to execute an action on an unsupported entity
        params = {
            "action_id": "add_history",
            "entity_type": "contact",
            "object_id": "contact123"
        }
        result = self.action_capability.execute_action(params)
        
        # Check the result
        self.assertFalse(result["success"])
        self.assertIn("not supported for entity type", result["error"])
    
    def test_execute_action_missing_params(self):
        """Test that execute_action returns an error for missing parameters."""
        # Try to execute an action without required parameters
        params = {
            "action_id": "attach_document",
            "entity_type": "deal",
            "object_id": "deal123"
        }
        result = self.action_capability.execute_action(params)
        
        # Check the result
        self.assertFalse(result["success"])
        self.assertIn("Missing required document parameters", result["error"])
    
    def test_execute_action_error_handling(self):
        """Test that execute_action handles errors correctly."""
        # Mock update_deal to raise an exception
        self.api_client.update_deal = MagicMock(side_effect=Exception("API Error"))
        
        # Try to execute an action
        params = {
            "action_id": "update",
            "entity_type": "deal",
            "object_id": "deal123",
            "properties": {"name": "Updated Deal"}
        }
        result = self.action_capability.execute_action(params)
        
        # Check the result
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "API Error")

if __name__ == '__main__':
    unittest.main()