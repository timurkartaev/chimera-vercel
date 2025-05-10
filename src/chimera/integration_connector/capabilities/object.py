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
    
    def _get_authentication_state(self) -> Dict[str, str]:
        """Get the current authentication state."""
        return {"status": "connected"}  # Default to connected for testing
    
    def get_objects(self, entity_type: str, entity_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve a list of available objects for a specific entity type.
        
        Args:
            entity_type: The type of entity to get objects for
            entity_id: The entity ID for subtypes
            
        Returns:
            List of objects with id and name
        """
        if self._get_authentication_state()["status"] != "connected":
            return []
            
        if entity_type not in self.config.get("objects", {}):
            return []
            
        try:
            endpoint = f"{entity_type}"
            response = self.api_client.get(endpoint)
            return response
        except Exception as e:
            logger.error(f"Error getting objects for {entity_type}: {str(e)}")
            return []
    
    def get_object(self, entity_type: str, object_id: str) -> Dict[str, Any]:
        """
        Retrieve a specific object.
        
        Args:
            entity_type: The type of entity
            object_id: The ID of the object to retrieve
            
        Returns:
            Object data
        """
        if self._get_authentication_state()["status"] != "connected":
            return {}
            
        if entity_type not in self.config.get("objects", {}):
            return {}
            
        try:
            endpoint = f"{entity_type}/{object_id}"
            return self.api_client.get(endpoint)
        except Exception as e:
            logger.error(f"Error getting object {object_id} for {entity_type}: {str(e)}")
            return {}
    
    def create_object(self, entity_type: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new object.
        
        Args:
            entity_type: The type of entity
            data: The data for the new object
            
        Returns:
            Created object data
        """
        endpoint = f"{entity_type}"
        return self.api_client.post(endpoint, data=data)
    
    def update_object(self, entity_type: str, object_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an object.
        
        Args:
            entity_type: The type of entity
            object_id: The ID of the object to update
            data: The data to update
            
        Returns:
            Updated object data
        """
        endpoint = f"{entity_type}/{object_id}"
        return self.api_client.put(endpoint, data=data)
    
    def delete_object(self, entity_type: str, object_id: str) -> None:
        """
        Delete an object.
        
        Args:
            entity_type: The type of entity
            object_id: The ID of the object to delete
        """
        endpoint = f"{entity_type}/{object_id}"
        self.api_client.delete(endpoint)
    
    def _get_deals(self) -> List[Dict[str, Any]]:
        """Get a list of deals."""
        response = self.api_client.get("deals")
        return response.get("deals", [])
    
    def _get_companies(self) -> List[Dict[str, Any]]:
        """Get a list of companies."""
        response = self.api_client.get("companies")
        return response.get("companies", [])
    
    def _get_contacts(self) -> List[Dict[str, Any]]:
        """Get a list of contacts."""
        response = self.api_client.get("contacts")
        contacts = response.get("contacts", [])
        return [{"id": c["id"], "name": f"{c['first_name']} {c['last_name']}"} for c in contacts]
    
    def _get_custom_objects(self, entity_id: str) -> List[Dict[str, Any]]:
        """Get a list of custom objects."""
        response = self.api_client.get(f"custom_objects/{entity_id}")
        return response.get("objects", [])
    
    def _get_deal_data(self, object_id: str) -> Dict[str, Any]:
        """Get deal data."""
        return self.api_client.get(f"deals/{object_id}")
    
    def _get_company_data(self, object_id: str) -> Dict[str, Any]:
        """Get company data."""
        return self.api_client.get(f"companies/{object_id}")
    
    def _get_contact_data(self, object_id: str) -> Dict[str, Any]:
        """Get contact data."""
        return self.api_client.get(f"contacts/{object_id}")
    
    def _get_custom_object_data(self, entity_id: str, object_id: str) -> Dict[str, Any]:
        """Get custom object data."""
        return self.api_client.get(f"custom_objects/{entity_id}/{object_id}")
    
    def _transform_custom_object(self, obj_data: Dict[str, Any], entity_id: str) -> Dict[str, Any]:
        """Transform custom object data."""
        return obj_data  # Return raw data for now