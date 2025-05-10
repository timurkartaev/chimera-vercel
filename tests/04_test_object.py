import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.capabilities.object import ObjectCapability
from chimera.integration_connector.api.client import ApiClient

@pytest.fixture
def mock_config():
    return {
        'objects': {
            'test_entity': {
                'fields': {
                    'id': {'type': 'string'},
                    'name': {'type': 'string'}
                }
            }
        }
    }

@pytest.fixture
def mock_api_client():
    return MagicMock(spec=ApiClient)

def test_object_capability_initialization(mock_config, mock_api_client):
    """Test object capability initialization."""
    capability = ObjectCapability(mock_config, mock_api_client)
    assert capability.api_client is not None

def test_get_objects(mock_config, mock_api_client):
    """Test getting objects."""
    capability = ObjectCapability(mock_config, mock_api_client)
    mock_api_client.get.return_value = [
        {'id': '1', 'name': 'Object 1'},
        {'id': '2', 'name': 'Object 2'}
    ]
    
    objects = capability.get_objects({'entity_type': 'test_entity'})
    assert len(objects) == 2
    mock_api_client.get.assert_called_once_with('test_entity')

def test_get_object(mock_config, mock_api_client):
    """Test getting a specific object."""
    capability = ObjectCapability(mock_config, mock_api_client)
    mock_api_client.get.return_value = {'id': '1', 'name': 'Object 1'}
    
    obj = capability.get_object({'entity_type': 'test_entity', 'object_id': '1'})
    assert obj['id'] == '1'
    assert obj['name'] == 'Object 1'
    mock_api_client.get.assert_called_once_with('test_entity/1')

def test_get_objects_unsupported_entity(mock_config, mock_api_client):
    """Test that get_objects returns an empty list for unsupported entity types."""
    capability = ObjectCapability(mock_config, mock_api_client)
    objects = capability.get_objects({'entity_type': 'unknown_type'})
    assert objects == []

def test_get_object_unsupported_entity(mock_config, mock_api_client):
    """Test that get_object returns an empty dict for unsupported entity types."""
    capability = ObjectCapability(mock_config, mock_api_client)
    obj = capability.get_object({'entity_type': 'unknown_type', 'object_id': '1'})
    assert obj == {}

def test_api_error_handling(mock_config, mock_api_client):
    """Test that API errors are handled gracefully."""
    capability = ObjectCapability(mock_config, mock_api_client)
    mock_api_client.get.side_effect = Exception("API Error")
    
    # Test get_objects error handling
    objects = capability.get_objects({'entity_type': 'test_entity'})
    assert objects == []
    
    # Test get_object error handling
    obj = capability.get_object({'entity_type': 'test_entity', 'object_id': '1'})
    assert obj == {}

if __name__ == '__main__':
    unittest.main()