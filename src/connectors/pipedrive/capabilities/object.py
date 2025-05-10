import logging
from typing import Dict, Any, List, Optional
from ..integration_connector.capabilities.object import ObjectCapability

logger = logging.getLogger(__name__)

class PipedriveObjectCapability(ObjectCapability):
    """
    Pipedrive object capability that extends the base object capability.
    Currently uses all base functionality without modifications.
    """
    pass

class ObjectCapability:
    """
    Implements the Object capability which handles read operations
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