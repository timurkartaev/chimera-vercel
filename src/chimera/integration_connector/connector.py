import os
import yaml
from .api.client import ApiClient
from .capabilities.info import InfoCapability
from .capabilities.localization import LocalizationCapability
from .capabilities.authorize import AuthorizeCapability
from .capabilities.entity import EntityCapability
from .capabilities.object import ObjectCapability
from .capabilities.action import ActionCapability

class IntegrationConnector:
    """
    Main Integration Connector class that implements all capabilities required
    for connecting PandaDoc with an external system.
    
    This class acts as a facade that delegates to specialized capability classes.
    """
    
    def __init__(self, config_path=None):
        """
        Initialize the connector with configuration and capabilities.
        
        Args:
            config_path (str, optional): Path to the config.yaml file. 
                                        Defaults to the config.yaml in the same directory.
        """
        if config_path is None:
            # Default to config.yaml in the same directory as this file
            config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        
        # Load configuration
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        # Create API client (will be used by capability implementations)
        self._api_client = ApiClient()
        
        # Initialize all capabilities
        self._setup_capabilities()
    
    def _setup_capabilities(self):
        """Set up all capability implementations."""
        self.info = InfoCapability(self.config, self._api_client)
        self.localization = LocalizationCapability(self.config, self._api_client)
        self.authorize = AuthorizeCapability(self.config, self._api_client)
        self.entity = EntityCapability(self.config, self._api_client)
        self.object = ObjectCapability(self.config, self._api_client)
        self.action = ActionCapability(self.config, self._api_client)
    
    # INFO CAPABILITY
    def get_info(self):
        """Return integration info metadata."""
        return self.info.get_info()
    
    # LOCALIZATION CAPABILITY
    def get_localization(self, lang='en'):
        """Return localization data for the specified language."""
        return self.localization.get_localization(lang)
    
    # AUTHORIZE CAPABILITY
    def get_authentication_state(self):
        """Get the current authentication state."""
        return self.authorize.get_authentication_state()
        
    def authorize(self, credentials):
        """
        Authorize with the external system using provided credentials.
        
        Args:
            credentials (dict): The credentials provided by the user
        
        Returns:
            dict: Authorization result with status
        """
        return self.authorize.authorize(credentials)
    
    # ENTITY CAPABILITY
    def get_entities(self):
        """
        Return all available entities for this integration.
        
        Returns:
            list: Array of entity definitions
        """
        return self.entity.get_entities()
    
    def get_entity_subtypes(self, entity_type):
        """
        Return a list of subtypes for a given entity type.
        
        Args:
            entity_type (str): The parent entity type
            
        Returns:
            list: Array of entity subtype definitions
        """
        return self.entity.get_entity_subtypes(entity_type)
    
    def get_entity_schema(self, entity_type, entity_id=None):
        """
        Return the schema for a specific entity type (and ID if needed).
        
        Args:
            entity_type (str): The entity type
            entity_id (str, optional): The entity ID for subtypes
            
        Returns:
            dict: JSON Schema definition of the entity
        """
        return self.entity.get_entity_schema(entity_type, entity_id)
    
    # OBJECT CAPABILITY
    def get_objects(self, entity_type, entity_id=None):
        """
        Retrieve a list of available objects for a specific entity type.
        
        Args:
            entity_type (str): The type of entity to get objects for
            entity_id (str, optional): The entity ID for subtypes
            
        Returns:
            list: Array of objects with id and name
        """
        return self.object.get_objects(entity_type, entity_id)
    
    def get_object_data(self, entity_type, entity_id, object_id):
        """
        Retrieve the complete data for a specific object.
        
        Args:
            entity_type (str): The type of entity
            entity_id (str, optional): The entity ID for subtypes
            object_id (str): The ID of the specific object to retrieve
            
        Returns:
            dict: Complete object data with all fields and values
        """
        return self.object.get_object_data(entity_type, entity_id, object_id)
    
    # ACTION CAPABILITY
    def get_actions(self, entity_type=None):
        """
        Return all available actions for this integration.
        
        Args:
            entity_type (str, optional): Filter actions for a specific entity type
        
        Returns:
            list: Array of action definitions with compatible entities
        """
        return self.action.get_actions(entity_type)
    
    def execute_action(self, action_id, entity_type, object_id, params):
        """
        Execute a specific action on an object.
        
        Args:
            action_id (str): The ID of the action to execute
            entity_type (str): The type of entity
            object_id (str): The ID of the object to perform the action on
            params (dict): Parameters required for the action
            
        Returns:
            dict: Result of the action execution
        """
        return self.action.execute_action(action_id, entity_type, object_id, params)