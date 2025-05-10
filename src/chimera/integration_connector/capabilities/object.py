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
        self._api_client = api_client
    
    def get_objects(self, entity_type: str, entity_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Retrieve a list of available objects for a specific entity type.
        
        Args:
            entity_type: The type of entity to get objects for
            entity_id: The entity ID for subtypes
            
        Returns:
            List of objects with id and name
        """
        if entity_type == "custom_object" and entity_id:
            endpoint = f"custom_objects/{entity_id}"
        else:
            endpoint = f"{entity_type}s"
            
        response = self._api_client.get(endpoint)
        return response.get("results", [])
    
    def get_object_data(self, entity_type: str, entity_id: Optional[str], object_id: str) -> Dict[str, Any]:
        """
        Retrieve the complete data for a specific object.
        
        Args:
            entity_type: The type of entity
            entity_id: The entity ID for subtypes
            object_id: The ID of the specific object to retrieve
            
        Returns:
            Complete object data with all fields and values
        """
        if entity_type == "custom_object" and entity_id:
            endpoint = f"custom_objects/{entity_id}/{object_id}"
        else:
            endpoint = f"{entity_type}s/{object_id}"
            
        return self._api_client.get(endpoint)
    
    def update_object(self, entity_type: str, entity_id: Optional[str], object_id: str, properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an object's properties.
        
        Args:
            entity_type: The type of entity
            entity_id: The entity ID for subtypes
            object_id: The ID of the object to update
            properties: The properties to update
            
        Returns:
            Updated object data
        """
        if entity_type == "custom_object" and entity_id:
            endpoint = f"custom_objects/{entity_id}/{object_id}"
        else:
            endpoint = f"{entity_type}s/{object_id}"
            
        return self._api_client.put(endpoint, json=properties)
    
    def create_object(self, entity_type: str, entity_id: Optional[str], properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new object.
        
        Args:
            entity_type: The type of entity
            entity_id: The entity ID for subtypes
            properties: The properties for the new object
            
        Returns:
            Created object data
        """
        if entity_type == "custom_object" and entity_id:
            endpoint = f"custom_objects/{entity_id}"
        else:
            endpoint = f"{entity_type}s"
            
        return self._api_client.post(endpoint, json=properties)
    
    def delete_object(self, entity_type: str, entity_id: Optional[str], object_id: str) -> None:
        """
        Delete an object.
        
        Args:
            entity_type: The type of entity
            entity_id: The entity ID for subtypes
            object_id: The ID of the object to delete
        """
        if entity_type == "custom_object" and entity_id:
            endpoint = f"custom_objects/{entity_id}/{object_id}"
        else:
            endpoint = f"{entity_type}s/{object_id}"
            
        self._api_client.delete(endpoint)
    
    def attach_document(self, entity_type: str, object_id: str, document_id: str, document_name: str, document_url: str) -> Dict[str, Any]:
        """
        Attach a document to an object.
        
        Args:
            entity_type: The type of entity
            object_id: The ID of the object
            document_id: The ID of the document
            document_name: The name of the document
            document_url: The URL of the document
            
        Returns:
            Attachment data
        """
        endpoint = f"{entity_type}s/{object_id}/documents"
        data = {
            "document_id": document_id,
            "document_name": document_name,
            "document_url": document_url
        }
        return self._api_client.post(endpoint, json=data)
    
    def add_activity(self, entity_type: str, object_id: str, activity_type: str, document_id: str, document_name: str, message: str) -> Dict[str, Any]:
        """
        Add an activity to an object.
        
        Args:
            entity_type: The type of entity
            object_id: The ID of the object
            activity_type: The type of activity
            document_id: The ID of the document
            document_name: The name of the document
            message: The activity message
            
        Returns:
            Activity data
        """
        endpoint = f"{entity_type}s/{object_id}/activities"
        data = {
            "type": activity_type,
            "document_id": document_id,
            "document_name": document_name,
            "message": message
        }
        return self._api_client.post(endpoint, json=data)