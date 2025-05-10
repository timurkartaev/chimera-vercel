import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.capabilities.entity import EntityCapability
from chimera.integration_connector.api.client import ApiClient

class TestEntityCapability(unittest.TestCase):
    """Test suite for the EntityCapability class."""
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock config
        self.config = {
            'entities': ['deal', 'company', 'contact']
        }
        
        # Create a mock API client
        self.api_client = MagicMock(spec=ApiClient)
        
        # Create an instance of the capability
        self.entity_capability = EntityCapability(self.config, self.api_client)
    
    def test_get_entities(self):
        """Test that get_entities returns the correct entities."""
        entities = self.entity_capability.get_entities()
        
        self.assertEqual(len(entities), 3)
        self.assertEqual(entities[0]["entity_type"], "deal")
        self.assertEqual(entities[1]["entity_type"], "company")
        self.assertEqual(entities[2]["entity_type"], "contact")
        self.assertFalse(entities[0]["has_entity_subtypes"])
    
    def test_get_entity_subtypes(self):
        """Test that get_entity_subtypes returns an empty list for standard entities."""
        params = {"entity_type": "deal"}
        subtypes = self.entity_capability.get_entity_subtypes(params)
        
        self.assertEqual(subtypes, [])
    
    def test_get_entity_schema(self):
        """Test that get_entity_schema returns the correct schema for a deal."""
        params = {"entity_type": "deal"}
        schema = self.entity_capability.get_entity_schema(params)
        
        self.assertEqual(schema["type"], "object")
        self.assertIn("properties", schema)
        self.assertIn("id", schema["properties"])
        self.assertIn("name", schema["properties"])
    
    def test_get_entity_schema_with_entity_id(self):
        """Test that get_entity_schema handles entity_id parameter."""
        params = {"entity_type": "custom_object", "entity_id": "123"}
        self.api_client.get.return_value = {
            "fields": [
                {
                    "id": "field1",
                    "name": "Field 1",
                    "type": "text"
                }
            ],
            "required_fields": ["field1"]
        }
        
        schema = self.entity_capability.get_entity_schema(params)
        
        self.assertEqual(schema["type"], "object")
        self.assertIn("field1", schema["properties"])
        self.assertEqual(schema["required"], ["field1"])
    
    def test_get_entity_schema_unknown_type(self):
        """Test that get_entity_schema returns a default schema for unknown types."""
        params = {"entity_type": "unknown_type"}
        schema = self.entity_capability.get_entity_schema(params)
        
        self.assertEqual(schema["type"], "object")
        self.assertEqual(schema["properties"], {})
    
    def test_get_entity_schema_invalid_type(self):
        """Test that get_entity_schema raises ValueError for invalid types."""
        params = {"entity_type": "invalid_type"}
        
        with self.assertRaises(ValueError):
            self.entity_capability.get_entity_schema(params)
    
    def test_register_entity(self):
        """Test registering a new entity."""
        entity = {
            "entity_type": "test_entity",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"}
                }
            }
        }
        
        self.entity_capability.register_entity(entity)
        
        self.assertEqual(len(self.entity_capability.entities), 1)
        self.assertEqual(self.entity_capability.entities[0], entity)
    
    def test_register_entity_duplicate(self):
        """Test registering a duplicate entity."""
        entity = {
            "entity_type": "test_entity",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"}
                }
            }
        }
        
        self.entity_capability.register_entity(entity)
        self.entity_capability.register_entity(entity)  # Register again
        
        self.assertEqual(len(self.entity_capability.entities), 1)  # Should not add duplicate
    
    def test_register_entity_invalid(self):
        """Test registering an invalid entity."""
        with self.assertRaises(ValueError):
            self.entity_capability.register_entity("not a dict")
        
        with self.assertRaises(ValueError):
            self.entity_capability.register_entity({})  # Missing entity_type
    
    def test_register_entity_default_schema(self):
        """Test registering an entity without a schema."""
        entity = {
            "entity_type": "test_entity"
        }
        
        self.entity_capability.register_entity(entity)
        
        self.assertEqual(len(self.entity_capability.entities), 1)
        self.assertEqual(self.entity_capability.entities[0]["schema"], {
            "type": "object",
            "properties": {}
        })

@pytest.fixture
def mock_config():
    """Create a mock config for testing."""
    return {
        'entities': [
            {
                'entity_type': 'test_entity',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'string'},
                        'name': {'type': 'string'}
                    }
                }
            }
        ]
    }

@pytest.fixture
def mock_api_client():
    """Create a mock API client for testing."""
    return MagicMock()

def test_entity_capability_initialization(mock_config, mock_api_client):
    """Test EntityCapability initialization."""
    capability = EntityCapability(mock_config, mock_api_client)
    assert capability.config == mock_config
    assert capability._api_client == mock_api_client
    assert capability.entities == []
    assert capability.static_entities == mock_config['entities']

def test_register_entity(mock_config, mock_api_client):
    """Test registering an entity."""
    capability = EntityCapability(mock_config, mock_api_client)
    entity = {
        'entity_type': 'test_entity',
        'schema': {
            'type': 'object',
            'properties': {
                'id': {'type': 'string'},
                'name': {'type': 'string'}
            }
        }
    }
    capability.register_entity(entity)
    assert len(capability.entities) == 1
    assert capability.entities[0] == entity

def test_get_entities(mock_config, mock_api_client):
    """Test getting all entities."""
    capability = EntityCapability(mock_config, mock_api_client)
    entities = capability.get_entities()
    assert len(entities) == 1
    assert entities[0]['entity_type'] == 'test_entity'

def test_get_entity_schema(mock_config, mock_api_client):
    """Test getting entity schema."""
    capability = EntityCapability(mock_config, mock_api_client)
    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'name': {'type': 'string'}
        }
    }
    entity = {
        'entity_type': 'test_entity',
        'schema': schema
    }
    capability.register_entity(entity)
    
    result = capability.get_entity_schema({"entity_type": "test_entity"})
    assert result == schema

def test_get_entity_schema_not_found(mock_config, mock_api_client):
    """Test getting schema for non-existent entity."""
    capability = EntityCapability(mock_config, mock_api_client)
    with pytest.raises(ValueError):
        capability.get_entity_schema({"entity_type": "non_existent"})

if __name__ == '__main__':
    unittest.main()