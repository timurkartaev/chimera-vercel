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
        self.config = {}
        
        # Create a mock API client
        self.api_client = MagicMock(spec=ApiClient)
        
        # Create an instance of the capability
        self.object_capability = ObjectCapability(self.config, self.api_client)
        
        # Mock the authentication state
        self.object_capability._get_authentication_state = MagicMock(return_value={"status": "connected"})
    
    def test_get_deals(self):
        """Test that _get_deals returns a list of deals."""
        # Mock the API response
        self.api_client.get_deals.return_value = {
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
    
    def test_get_companies(self):
        """Test that _get_companies returns a list of companies."""
        # Mock the API response
        self.api_client.get_companies.return_value = {
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
    
    def test_get_contacts(self):
        """Test that _get_contacts returns a list of contacts."""
        # Mock the API response
        self.api_client.get_contacts.return_value = {
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
    
    def test_get_custom_objects(self):
        """Test that _get_custom_objects returns a list of custom objects."""
        # Mock the API response
        self.api_client.get_custom_objects.return_value = {
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
        self.api_client.get_custom_objects.assert_called_once_with("product")
    
    def test_get_objects(self):
        """Test that get_objects delegates to the correct method based on entity type."""
        # Mock the individual methods
        self.object_capability._get_deals = MagicMock(return_value=[
            {"id": "deal1", "name": "Test Deal"}
        ])
        self.object_capability._get_companies = MagicMock(return_value=[
            {"id": "company1", "name": "Test Company"}
        ])
        self.object_capability._get_contacts = MagicMock(return_value=[
            {"id": "contact1", "name": "Test Contact"}
        ])
        self.object_capability._get_custom_objects = MagicMock(return_value=[
            {"id": "obj1", "name": "Test Object"}
        ])
        
        # Test each entity type
        self.assertEqual(self.object_capability.get_objects("deal"), [{"id": "deal1", "name": "Test Deal"}])
        self.assertEqual(self.object_capability.get_objects("company"), [{"id": "company1", "name": "Test Company"}])
        self.assertEqual(self.object_capability.get_objects("contact"), [{"id": "contact1", "name": "Test Contact"}])
        self.assertEqual(self.object_capability.get_objects("custom_object", "product"), [{"id": "obj1", "name": "Test Object"}])
        
        # Verify method calls
        self.object_capability._get_deals.assert_called_once()
        self.object_capability._get_companies.assert_called_once()
        self.object_capability._get_contacts.assert_called_once()
        self.object_capability._get_custom_objects.assert_called_once_with("product")
    
    def test_get_objects_not_authenticated(self):
        """Test that get_objects returns an empty list when not authenticated."""
        # Mock authentication state to return disconnected
        self.object_capability._get_authentication_state = MagicMock(return_value={"status": "disconnected"})
        
        # Try to get objects
        objects = self.object_capability.get_objects("deal")
        
        # Check the result
        self.assertEqual(objects, [])
    
    def test_get_objects_unsupported_entity(self):
        """Test that get_objects returns an empty list for unsupported entity types."""
        objects = self.object_capability.get_objects("unknown_type")
        
        self.assertEqual(objects, [])
    
    def test_get_deal_data(self):
        """Test that _get_deal_data returns the correct deal data."""
        # Mock the API response
        self.api_client.get_deal.return_value = {
            "id": "deal1",
            "name": "Test Deal",
            "amount": 5000,
            "stage": "Proposal",
            "close_date": "2023-12-31",
            "owner": {
                "id": "user1",
                "name": "John Owner",
                "email": "john@example.com"
            },
            "contacts": [
                {
                    "id": "contact1",
                    "name": "Jane Contact",
                    "email": "jane@example.com"
                }
            ]
        }
        
        # Get deal data
        deal_data = self.object_capability._get_deal_data("deal1")
        
        # Check the data
        self.assertEqual(deal_data["id"], "deal1")
        self.assertEqual(deal_data["name"], "Test Deal")
        self.assertEqual(deal_data["amount"], 5000)
        self.assertEqual(deal_data["stage"], "Proposal")
        self.assertEqual(deal_data["close_date"], "2023-12-31")
        self.assertEqual(deal_data["owner"]["id"], "user1")
        self.assertEqual(deal_data["owner"]["name"], "John Owner")
        self.assertEqual(deal_data["contacts"][0]["id"], "contact1")
        self.assertEqual(deal_data["contacts"][0]["name"], "Jane Contact")
        
        # Verify API call
        self.api_client.get_deal.assert_called_once_with("deal1")
    
    def test_get_company_data(self):
        """Test that _get_company_data returns the correct company data."""
        # Mock the API response
        self.api_client.get_company.return_value = {
            "id": "company1",
            "name": "Test Company",
            "domain": "example.com",
            "industry": "Technology",
            "size": "51-200",
            "address": {
                "street": "123 Main St",
                "city": "San Francisco",
                "state": "CA",
                "postal_code": "94105",
                "country": "USA"
            }
        }
        
        # Get company data
        company_data = self.object_capability._get_company_data("company1")
        
        # Check the data
        self.assertEqual(company_data["id"], "company1")
        self.assertEqual(company_data["name"], "Test Company")
        self.assertEqual(company_data["domain"], "example.com")
        self.assertEqual(company_data["industry"], "Technology")
        self.assertEqual(company_data["address"]["street"], "123 Main St")
        self.assertEqual(company_data["address"]["city"], "San Francisco")
        
        # Verify API call
        self.api_client.get_company.assert_called_once_with("company1")
    
    def test_get_contact_data(self):
        """Test that _get_contact_data returns the correct contact data."""
        # Mock the API response
        self.api_client.get_contact.return_value = {
            "id": "contact1",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone": "555-1234",
            "job_title": "CEO",
            "company": {
                "id": "company1",
                "name": "Test Company"
            }
        }
        
        # Get contact data
        contact_data = self.object_capability._get_contact_data("contact1")
        
        # Check the data
        self.assertEqual(contact_data["id"], "contact1")
        self.assertEqual(contact_data["first_name"], "John")
        self.assertEqual(contact_data["last_name"], "Doe")
        self.assertEqual(contact_data["email"], "john@example.com")
        self.assertEqual(contact_data["phone"], "555-1234")
        self.assertEqual(contact_data["job_title"], "CEO")
        self.assertEqual(contact_data["company"]["id"], "company1")
        self.assertEqual(contact_data["company"]["name"], "Test Company")
        
        # Verify API call
        self.api_client.get_contact.assert_called_once_with("contact1")
    
    def test_get_custom_object_data(self):
        """Test that _get_custom_object_data returns the correct custom object data."""
        # Mock the API response
        self.api_client.get_custom_object.return_value = {
            "id": "obj1",
            "name": "Test Object",
            "custom_field": "custom value"
        }
        
        # Mock the transform method to return the raw data
        self.object_capability._transform_custom_object = MagicMock(
            side_effect=lambda obj_data, entity_id: obj_data
        )
        
        # Get custom object data
        obj_data = self.object_capability._get_custom_object_data("product", "obj1")
        
        # Check the data
        self.assertEqual(obj_data["id"], "obj1")
        self.assertEqual(obj_data["name"], "Test Object")
        self.assertEqual(obj_data["custom_field"], "custom value")
        
        # Verify API call
        self.api_client.get_custom_object.assert_called_once_with("product", "obj1")
        self.object_capability._transform_custom_object.assert_called_once()
    
    def test_get_object_data(self):
        """Test that get_object_data delegates to the correct method based on entity type."""
        # Mock the individual methods
        self.object_capability._get_deal_data = MagicMock(return_value={"id": "deal1", "name": "Test Deal"})
        self.object_capability._get_company_data = MagicMock(return_value={"id": "company1", "name": "Test Company"})
        self.object_capability._get_contact_data = MagicMock(return_value={"id": "contact1", "name": "Test Contact"})
        self.object_capability._get_custom_object_data = MagicMock(return_value={"id": "obj1", "name": "Test Object"})
        
        # Test each entity type
        self.assertEqual(self.object_capability.get_object_data("deal", None, "deal1"), {"id": "deal1", "name": "Test Deal"})
        self.assertEqual(self.object_capability.get_object_data("company", None, "company1"), {"id": "company1", "name": "Test Company"})
        self.assertEqual(self.object_capability.get_object_data("contact", None, "contact1"), {"id": "contact1", "name": "Test Contact"})
        self.assertEqual(self.object_capability.get_object_data("custom_object", "product", "obj1"), {"id": "obj1", "name": "Test Object"})
        
        # Verify method calls
        self.object_capability._get_deal_data.assert_called_once_with("deal1")
        self.object_capability._get_company_data.assert_called_once_with("company1")
        self.object_capability._get_contact_data.assert_called_once_with("contact1")
        self.object_capability._get_custom_object_data.assert_called_once_with("product", "obj1")
    
    def test_get_object_data_not_authenticated(self):
        """Test that get_object_data returns an empty dict when not authenticated."""
        # Mock authentication state to return disconnected
        self.object_capability._get_authentication_state = MagicMock(return_value={"status": "disconnected"})
        
        # Try to get object data
        data = self.object_capability.get_object_data("deal", None, "deal1")
        
        # Check the result
        self.assertEqual(data, {})
    
    def test_get_object_data_unsupported_entity(self):
        """Test that get_object_data returns an empty dict for unsupported entity types."""
        data = self.object_capability.get_object_data("unknown_type", None, "obj1")
        
        self.assertEqual(data, {})
    
    def test_transform_custom_object(self):
        """Test that _transform_custom_object returns the raw data."""
        obj_data = {"id": "obj1", "name": "Test Object", "custom_field": "custom value"}
        transformed = self.object_capability._transform_custom_object(obj_data, "product")
        
        # In our simplified implementation, this just returns the raw data
        self.assertEqual(transformed, obj_data)
    
    def test_api_error_handling(self):
        """Test that API errors are handled gracefully."""
        # Mock API method to raise an exception
        self.api_client.get_deals.side_effect = Exception("API error")
        
        # Try to get deals
        deals = self.object_capability._get_deals()
        
        # Check that it returns an empty list on error
        self.assertEqual(deals, [])

if __name__ == '__main__':
    unittest.main()