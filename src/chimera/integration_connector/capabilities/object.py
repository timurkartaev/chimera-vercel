import logging
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class ObjectCapability:
    """
    Implements the Object capability which handles CRUD operations
    for different entity types.
    """
    
    def __init__(self, config, api_client):
        """
        Initialize the Object capability.
        
        Args:
            config (dict): The integration configuration
            api_client (ApiClient): The API client instance
        """
        self.config = config
        self.api_client = api_client
    
    def get_objects(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Retrieve a list of available objects for a specific entity type.
        
        Args:
            params: Dictionary containing:
                - entity_type: The type of entity to get objects for
                - entity_id: Optional entity ID for subtypes
            
        Returns:
            List of objects with id and name
        """
        entity_type = params.get('entity_type')
        if entity_type not in self.config.get("objects", {}):
            return []
            
        try:
            endpoint = f"{entity_type}"
            response = self.api_client.get(endpoint)
            return response
        except Exception as e:
            logger.error(f"Error getting objects for {entity_type}: {str(e)}")
            return []
    
    def get_object(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Retrieve a specific object.
        
        Args:
            params: Dictionary containing:
                - entity_type: The type of entity
                - object_id: The ID of the object to retrieve
            
        Returns:
            Object data
        """
        entity_type = params.get('entity_type')
        object_id = params.get('object_id')
        
        if entity_type not in self.config.get("objects", {}):
            return {}
            
        try:
            endpoint = f"{entity_type}/{object_id}"
            return self.api_client.get(endpoint)
        except Exception as e:
            logger.error(f"Error getting object {object_id} for {entity_type}: {str(e)}")
            return {}
    
    def create_object(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new object.
        
        Args:
            params: Dictionary containing:
                - entity_type: The type of entity
                - data: The data for the new object
            
        Returns:
            Created object data
        """
        entity_type = params.get('entity_type')
        data = params.get('data', {})
        
        endpoint = f"{entity_type}"
        return self.api_client.post(endpoint, data=data)
    
    def update_object(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an object.
        
        Args:
            params: Dictionary containing:
                - entity_type: The type of entity
                - object_id: The ID of the object to update
                - data: The data to update
            
        Returns:
            Updated object data
        """
        entity_type = params.get('entity_type')
        object_id = params.get('object_id')
        data = params.get('data', {})
        
        endpoint = f"{entity_type}/{object_id}"
        return self.api_client.put(endpoint, data=data)
    
    def delete_object(self, params: Dict[str, Any]) -> None:
        """
        Delete an object.
        
        Args:
            params: Dictionary containing:
                - entity_type: The type of entity
                - object_id: The ID of the object to delete
        """
        entity_type = params.get('entity_type')
        object_id = params.get('object_id')
        
        endpoint = f"{entity_type}/{object_id}"
        self.api_client.delete(endpoint)
    
    def _get_deals(self, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Get a list of deals.
        
        Args:
            params: Optional dictionary containing any additional parameters
            
        Returns:
            List of deals
        """
        response = self.api_client.get("deals")
        return response.get("deals", [])
    
    def _get_companies(self, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Get a list of companies.
        
        Args:
            params: Optional dictionary containing any additional parameters
            
        Returns:
            List of companies
        """
        response = self.api_client.get("companies")
        return response.get("companies", [])
    
    def _get_contacts(self, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Get a list of contacts.
        
        Args:
            params: Optional dictionary containing any additional parameters
            
        Returns:
            List of contacts with id and name
        """
        response = self.api_client.get("contacts")
        contacts = response.get("contacts", [])
        return [{"id": c["id"], "name": f"{c['first_name']} {c['last_name']}"} for c in contacts]
    
    def _get_custom_objects(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Get a list of custom objects.
        
        Args:
            params: Dictionary containing:
                - entity_id: The ID of the custom object type
            
        Returns:
            List of custom objects
        """
        entity_id = params.get('entity_id')
        response = self.api_client.get(f"custom_objects/{entity_id}")
        return response.get("objects", [])
    
    def _get_deal_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get deal data.
        
        Args:
            params: Dictionary containing:
                - object_id: The ID of the deal
            
        Returns:
            Deal data
        """
        object_id = params.get('object_id')
        return self.api_client.get(f"deals/{object_id}")
    
    def _get_company_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get company data.
        
        Args:
            params: Dictionary containing:
                - object_id: The ID of the company
            
        Returns:
            Company data
        """
        object_id = params.get('object_id')
        return self.api_client.get(f"companies/{object_id}")
    
    def _get_contact_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get contact data.
        
        Args:
            params: Dictionary containing:
                - object_id: The ID of the contact
            
        Returns:
            Contact data
        """
        object_id = params.get('object_id')
        return self.api_client.get(f"contacts/{object_id}")
    
    def _get_custom_object_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get custom object data.
        
        Args:
            params: Dictionary containing:
                - entity_id: The ID of the custom object type
                - object_id: The ID of the custom object
            
        Returns:
            Custom object data
        """
        entity_id = params.get('entity_id')
        object_id = params.get('object_id')
        return self.api_client.get(f"custom_objects/{entity_id}/{object_id}")
    
    def _transform_custom_object(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform custom object data.
        
        Args:
            params: Dictionary containing:
                - obj_data: The object data to transform
                - entity_id: The ID of the custom object type
            
        Returns:
            Transformed object data
        """
        obj_data = params.get('obj_data', {})
        return obj_data  # Return raw data for now