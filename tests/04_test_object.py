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
    
    objects = capability.get_objects('test_entity')
    assert len(objects) == 2
    mock_api_client.get.assert_called_once_with('test_entity')

def test_get_object(mock_config, mock_api_client):
    """Test getting a specific object."""
    capability = ObjectCapability(mock_config, mock_api_client)
    mock_api_client.get.return_value = {'id': '1', 'name': 'Object 1'}
    
    obj = capability.get_object('test_entity', '1')
    assert obj['id'] == '1'
    assert obj['name'] == 'Object 1'
    mock_api_client.get.assert_called_once_with('test_entity/1')

def test_create_object(mock_config, mock_api_client):
    """Test creating an object."""
    capability = ObjectCapability(mock_config, mock_api_client)
    mock_api_client.post.return_value = {'id': '1', 'name': 'New Object'}
    
    data = {'name': 'New Object'}
    obj = capability.create_object('test_entity', data)
    assert obj['id'] == '1'
    assert obj['name'] == 'New Object'
    mock_api_client.post.assert_called_once_with('test_entity', data=data)

def test_update_object(mock_config, mock_api_client):
    """Test updating an object."""
    capability = ObjectCapability(mock_config, mock_api_client)
    mock_api_client.put.return_value = {'id': '1', 'name': 'Updated Object'}
    
    data = {'name': 'Updated Object'}
    obj = capability.update_object('test_entity', '1', data)
    assert obj['id'] == '1'
    assert obj['name'] == 'Updated Object'
    mock_api_client.put.assert_called_once_with('test_entity/1', data=data)

def test_delete_object(mock_config, mock_api_client):
    """Test deleting an object."""
    capability = ObjectCapability(mock_config, mock_api_client)
    
    capability.delete_object('test_entity', '1')
    mock_api_client.delete.assert_called_once_with('test_entity/1')

class TestObjectCapability(unittest.TestCase):
    """Test suite for the ObjectCapability class."""
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock config
        self.config = {
            'objects': {
                'test_entity': {
                    'fields': {
                        'id': {'type': 'string'},
                        'name': {'type': 'string'}
                    }
                }
            }
        }
        
        # Create a mock API client
        self.api_client = MagicMock(spec=ApiClient)
        
        # Create an instance of the capability
        self.object_capability = ObjectCapability(self.config, self.api_client)
    
    def test_get_deals(self):
        """Test that _get_deals returns a list of deals."""
        # Mock the API response
        self.api_client.get.return_value = {
            "deals": [
                {"id": "deal1", "name": "Test Deal 1"},
                {"id": "deal2", "name": "Test Deal 2"}
            ]
        }
        
        # Get deals
        deals = self.object_capability._get_deals()
        
        # Check the deals
        self.assertEqual(len(deals), 2)
        self.assertEqual(deals[0]["id"], "deal1")
        self.assertEqual(deals[0]["name"], "Test Deal 1")
        self.assertEqual(deals[1]["id"], "deal2")
        self.assertEqual(deals[1]["name"], "Test Deal 2")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("deals")
    
    def test_get_companies(self):
        """Test that _get_companies returns a list of companies."""
        # Mock the API response
        self.api_client.get.return_value = {
            "companies": [
                {"id": "company1", "name": "Test Company 1"},
                {"id": "company2", "name": "Test Company 2"}
            ]
        }
        
        # Get companies
        companies = self.object_capability._get_companies()
        
        # Check the companies
        self.assertEqual(len(companies), 2)
        self.assertEqual(companies[0]["id"], "company1")
        self.assertEqual(companies[0]["name"], "Test Company 1")
        self.assertEqual(companies[1]["id"], "company2")
        self.assertEqual(companies[1]["name"], "Test Company 2")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("companies")
    
    def test_get_contacts(self):
        """Test that _get_contacts returns a list of contacts."""
        # Mock the API response
        self.api_client.get.return_value = {
            "contacts": [
                {"id": "contact1", "first_name": "John", "last_name": "Doe"},
                {"id": "contact2", "first_name": "Jane", "last_name": "Smith"}
            ]
        }
        
        # Get contacts
        contacts = self.object_capability._get_contacts()
        
        # Check the contacts
        self.assertEqual(len(contacts), 2)
        self.assertEqual(contacts[0]["id"], "contact1")
        self.assertEqual(contacts[0]["name"], "John Doe")
        self.assertEqual(contacts[1]["id"], "contact2")
        self.assertEqual(contacts[1]["name"], "Jane Smith")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("contacts")
    
    def test_get_custom_objects(self):
        """Test that _get_custom_objects returns a list of custom objects."""
        # Mock the API response
        self.api_client.get.return_value = {
            "objects": [
                {"id": "obj1", "name": "Custom Object 1"},
                {"id": "obj2", "name": "Custom Object 2"}
            ]
        }
        
        # Get custom objects
        objects = self.object_capability._get_custom_objects("product")
        
        # Check the objects
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0]["id"], "obj1")
        self.assertEqual(objects[0]["name"], "Custom Object 1")
        self.assertEqual(objects[1]["id"], "obj2")
        self.assertEqual(objects[1]["name"], "Custom Object 2")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("custom_objects/product")
    
    def test_get_objects(self):
        """Test that get_objects delegates to the correct method based on entity type."""
        # Mock the API response
        self.api_client.get.return_value = [
            {"id": "obj1", "name": "Test Object"}
        ]
        
        # Test getting objects
        objects = self.object_capability.get_objects("test_entity")
        
        # Check the objects
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0]["id"], "obj1")
        self.assertEqual(objects[0]["name"], "Test Object")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("test_entity")
    
    def test_get_objects_unsupported_entity(self):
        """Test that get_objects returns an empty list for unsupported entity types."""
        objects = self.object_capability.get_objects("unknown_type")
        
        self.assertEqual(objects, [])
    
    def test_get_deal_data(self):
        """Test that _get_deal_data returns the correct deal data."""
        # Mock the API response
        self.api_client.get.return_value = {
            "id": "deal1",
            "name": "Test Deal",
            "amount": 5000,
            "stage": "Proposal",
            "close_date": "2023-12-31",
            "owner": {
                "id": "user1",
                "name": "John Owner"
            }
        }
        
        # Get deal data
        deal = self.object_capability._get_deal_data("deal1")
        
        # Check the deal data
        self.assertEqual(deal["id"], "deal1")
        self.assertEqual(deal["name"], "Test Deal")
        self.assertEqual(deal["amount"], 5000)
        self.assertEqual(deal["stage"], "Proposal")
        self.assertEqual(deal["close_date"], "2023-12-31")
        self.assertEqual(deal["owner"]["id"], "user1")
        self.assertEqual(deal["owner"]["name"], "John Owner")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("deals/deal1")
    
    def test_get_company_data(self):
        """Test that _get_company_data returns the correct company data."""
        # Mock the API response
        self.api_client.get.return_value = {
            "id": "company1",
            "name": "Test Company",
            "domain": "testcompany.com",
            "industry": "Technology",
            "size": "51-200",
            "address": {
                "street": "123 Test St",
                "city": "Test City",
                "state": "Test State",
                "postal_code": "12345",
                "country": "Test Country"
            }
        }
        
        # Get company data
        company = self.object_capability._get_company_data("company1")
        
        # Check the company data
        self.assertEqual(company["id"], "company1")
        self.assertEqual(company["name"], "Test Company")
        self.assertEqual(company["domain"], "testcompany.com")
        self.assertEqual(company["industry"], "Technology")
        self.assertEqual(company["size"], "51-200")
        self.assertEqual(company["address"]["street"], "123 Test St")
        self.assertEqual(company["address"]["city"], "Test City")
        self.assertEqual(company["address"]["state"], "Test State")
        self.assertEqual(company["address"]["postal_code"], "12345")
        self.assertEqual(company["address"]["country"], "Test Country")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("companies/company1")
    
    def test_get_contact_data(self):
        """Test that _get_contact_data returns the correct contact data."""
        # Mock the API response
        self.api_client.get.return_value = {
            "id": "contact1",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1-555-0123",
            "title": "CEO",
            "company": {
                "id": "company1",
                "name": "Test Company"
            }
        }
        
        # Get contact data
        contact = self.object_capability._get_contact_data("contact1")
        
        # Check the contact data
        self.assertEqual(contact["id"], "contact1")
        self.assertEqual(contact["first_name"], "John")
        self.assertEqual(contact["last_name"], "Doe")
        self.assertEqual(contact["email"], "john.doe@example.com")
        self.assertEqual(contact["phone"], "+1-555-0123")
        self.assertEqual(contact["title"], "CEO")
        self.assertEqual(contact["company"]["id"], "company1")
        self.assertEqual(contact["company"]["name"], "Test Company")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("contacts/contact1")
    
    def test_get_custom_object_data(self):
        """Test that _get_custom_object_data returns the correct custom object data."""
        # Mock the API response
        self.api_client.get.return_value = {
            "id": "obj1",
            "name": "Custom Object 1",
            "fields": {
                "field1": "value1",
                "field2": "value2"
            }
        }
        
        # Get custom object data
        obj = self.object_capability._get_custom_object_data("product", "obj1")
        
        # Check the custom object data
        self.assertEqual(obj["id"], "obj1")
        self.assertEqual(obj["name"], "Custom Object 1")
        self.assertEqual(obj["fields"]["field1"], "value1")
        self.assertEqual(obj["fields"]["field2"], "value2")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("custom_objects/product/obj1")
    
    def test_get_object_data(self):
        """Test that get_object_data delegates to the correct method based on entity type."""
        # Mock the API response
        self.api_client.get.return_value = {
            "id": "obj1",
            "name": "Test Object"
        }
        
        # Test getting object data
        obj = self.object_capability.get_object("test_entity", "obj1")
        
        # Check the object data
        self.assertEqual(obj["id"], "obj1")
        self.assertEqual(obj["name"], "Test Object")
        
        # Verify API call
        self.api_client.get.assert_called_once_with("test_entity/obj1")
    
    def test_get_object_data_unsupported_entity(self):
        """Test that get_object_data returns an empty dict for unsupported entity types."""
        obj = self.object_capability.get_object("unknown_type", "obj1")
        
        self.assertEqual(obj, {})
    
    def test_transform_custom_object(self):
        """Test that _transform_custom_object transforms the data correctly."""
        # Test data
        obj_data = {
            "id": "obj1",
            "name": "Custom Object 1",
            "fields": {
                "field1": "value1",
                "field2": "value2"
            }
        }
        
        # Transform the data
        transformed = self.object_capability._transform_custom_object(obj_data, "product")
        
        # Check the transformed data
        self.assertEqual(transformed, obj_data)  # Currently returns raw data
    
    def test_api_error_handling(self):
        """Test that API errors are handled gracefully."""
        # Mock the API client to raise an exception
        self.api_client.get.side_effect = Exception("API Error")
        
        # Test getting objects
        objects = self.object_capability.get_objects("test_entity")
        
        # Check that an empty list is returned
        self.assertEqual(objects, [])
        
        # Test getting object data
        obj = self.object_capability.get_object("test_entity", "obj1")
        
        # Check that an empty dict is returned
        self.assertEqual(obj, {})

if __name__ == '__main__':
    unittest.main()