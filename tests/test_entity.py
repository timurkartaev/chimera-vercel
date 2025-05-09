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
        subtypes = self.entity_capability.get_entity_subtypes("deal")
        
        self.assertEqual(subtypes, [])
    
    def test_get_entity_subtypes_custom_object(self):
        """Test that get_entity_subtypes returns custom object types."""
        # Mock the API response
        self.api_client.get.return_value = {
            "results": [
                {"id": "product", "name": "Product"},
                {"id": "project", "name": "Project"}
            ]
        }
        
        # Override _has_custom_objects_enabled to return True
        self.entity_capability._has_custom_objects_enabled = MagicMock(return_value=True)
        
        # Get custom object subtypes
        subtypes = self.entity_capability.get_entity_subtypes("custom_object")
        
        # Check the subtypes
        self.assertEqual(len(subtypes), 2)
        self.assertEqual(subtypes[0]["entity_id"], "product")
        self.assertEqual(subtypes[0]["name"], "Product")
        self.assertEqual(subtypes[1]["entity_id"], "project")
        self.assertEqual(subtypes[1]["name"], "Project")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("custom_objects")
    
    def test_get_entity_schema_deal(self):
        """Test that get_entity_schema returns the correct schema for deals."""
        schema = self.entity_capability.get_entity_schema("deal")
        
        # Check schema structure
        self.assertEqual(schema["type"], "object")
        self.assertIn("properties", schema)
        self.assertIn("id", schema["properties"])
        self.assertIn("name", schema["properties"])
        self.assertIn("amount", schema["properties"])
        self.assertIn("stage", schema["properties"])
        self.assertIn("owner", schema["properties"])
        self.assertIn("contacts", schema["properties"])
        
        # Check field types
        self.assertEqual(schema["properties"]["id"]["type"], "string")
        self.assertEqual(schema["properties"]["name"]["type"], "string")
        self.assertEqual(schema["properties"]["amount"]["type"], "number")
        self.assertEqual(schema["properties"]["owner"]["type"], "object")
        self.assertEqual(schema["properties"]["contacts"]["type"], "array")
        
        # Check required fields
        self.assertIn("required", schema)
        self.assertIn("id", schema["required"])
        self.assertIn("name", schema["required"])
    
    def test_get_entity_schema_company(self):
        """Test that get_entity_schema returns the correct schema for companies."""
        schema = self.entity_capability.get_entity_schema("company")
        
        # Check schema structure
        self.assertEqual(schema["type"], "object")
        self.assertIn("properties", schema)
        self.assertIn("id", schema["properties"])
        self.assertIn("name", schema["properties"])
        self.assertIn("domain", schema["properties"])
        self.assertIn("industry", schema["properties"])
        self.assertIn("size", schema["properties"])
        self.assertIn("address", schema["properties"])
        
        # Check field types
        self.assertEqual(schema["properties"]["id"]["type"], "string")
        self.assertEqual(schema["properties"]["name"]["type"], "string")
        self.assertEqual(schema["properties"]["address"]["type"], "object")
        
        # Check required fields
        self.assertIn("required", schema)
        self.assertIn("id", schema["required"])
        self.assertIn("name", schema["required"])
    
    def test_get_entity_schema_contact(self):
        """Test that get_entity_schema returns the correct schema for contacts."""
        schema = self.entity_capability.get_entity_schema("contact")
        
        # Check schema structure
        self.assertEqual(schema["type"], "object")
        self.assertIn("properties", schema)
        self.assertIn("id", schema["properties"])
        self.assertIn("first_name", schema["properties"])
        self.assertIn("last_name", schema["properties"])
        self.assertIn("email", schema["properties"])
        self.assertIn("phone", schema["properties"])
        self.assertIn("job_title", schema["properties"])
        self.assertIn("company", schema["properties"])
        
        # Check field types
        self.assertEqual(schema["properties"]["id"]["type"], "string")
        self.assertEqual(schema["properties"]["first_name"]["type"], "string")
        self.assertEqual(schema["properties"]["last_name"]["type"], "string")
        self.assertEqual(schema["properties"]["email"]["type"], "string")
        self.assertEqual(schema["properties"]["email"]["format"], "email")
        self.assertEqual(schema["properties"]["company"]["type"], "object")
        
        # Check required fields
        self.assertIn("required", schema)
        self.assertIn("id", schema["required"])
        self.assertIn("email", schema["required"])
    
    def test_get_entity_schema_custom_object(self):
        """Test that get_entity_schema returns the correct schema for custom objects."""
        # Mock the API response
        self.api_client.get.return_value = {
            "fields": [
                {"id": "id", "name": "ID", "type": "text", "readonly": True},
                {"id": "name", "name": "Name", "type": "text"},
                {"id": "amount", "name": "Amount", "type": "number"},
                {"id": "is_active", "name": "Is Active", "type": "boolean"}
            ]
        }
        
        # Get custom object schema
        schema = self.entity_capability.get_entity_schema("custom_object", "product")
        
        # Check schema structure
        self.assertEqual(schema["type"], "object")
        self.assertIn("properties", schema)
        self.assertEqual(len(schema["properties"]), 4)
        
        # Check mapped field types
        self.assertEqual(schema["properties"]["id"]["type"], "string")
        self.assertEqual(schema["properties"]["amount"]["type"], "number")
        self.assertEqual(schema["properties"]["is_active"]["type"], "boolean")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("custom_objects/product/schema")
    
    def test_get_entity_schema_unknown(self):
        """Test that get_entity_schema returns an empty schema for unknown entity types."""
        schema = self.entity_capability.get_entity_schema("unknown_type")
        
        self.assertEqual(schema["type"], "object")
        self.assertEqual(schema["properties"], {})
    
    def test_map_field_type(self):
        """Test that _map_field_type correctly maps external types to JSON Schema types."""
        # Test various field types
        self.assertEqual(self.entity_capability._map_field_type("text"), "string")
        self.assertEqual(self.entity_capability._map_field_type("number"), "number")
        self.assertEqual(self.entity_capability._map_field_type("boolean"), "boolean")
        self.assertEqual(self.entity_capability._map_field_type("date"), "string")
        self.assertEqual(self.entity_capability._map_field_type("picklist"), "string")
        self.assertEqual(self.entity_capability._map_field_type("lookup"), "object")
        self.assertEqual(self.entity_capability._map_field_type("currency"), "number")
        
        # Test unknown type (should default to string)
        self.assertEqual(self.entity_capability._map_field_type("unknown_type"), "string")
    
    def test_has_custom_objects_enabled(self):
        """Test that _has_custom_objects_enabled returns the correct value."""
        # By default it returns True in our implementation
        self.assertTrue(self.entity_capability._has_custom_objects_enabled())

@pytest.fixture
def mock_config():
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
    return MagicMock(spec=ApiClient)

def test_entity_capability_initialization(mock_config, mock_api_client):
    """Test entity capability initialization."""
    capability = EntityCapability(mock_config, mock_api_client)
    assert capability.entities == []

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
    entity1 = {'entity_type': 'entity1'}
    entity2 = {'entity_type': 'entity2'}
    capability.register_entity(entity1)
    capability.register_entity(entity2)
    
    entities = capability.get_entities()
    assert len(entities) == 2
    assert entity1 in entities
    assert entity2 in entities

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
    
    result = capability.get_entity_schema('test_entity')
    assert result == schema

def test_get_entity_schema_not_found(mock_config, mock_api_client):
    """Test getting schema for non-existent entity."""
    capability = EntityCapability(mock_config, mock_api_client)
    with pytest.raises(ValueError):
        capability.get_entity_schema('non_existent')

if __name__ == '__main__':
    unittest.main()