import os
import yaml
from ..integration-connector.connector import IntegrationConnector as BaseConnector
from .api.client import PipedriveApiClient
from ..integration-connector.capabilities.info import InfoCapability
from ..integration-connector.capabilities.localization import LocalizationCapability
from ..integration-connector.capabilities.authorize import AuthorizeCapability
from ..integration-connector.capabilities.entity import EntityCapability
from ..integration-connector.capabilities.object import ObjectCapability
from ..integration-connector.capabilities.action import ActionCapability

class PipedriveConnector:
    """
    Pipedrive connector implementation that extends the base connector functionality.
    """
    
    def __init__(self, config_path=None):
        """
        Initialize the connector with configuration and capabilities.
        
        Args:
            config_path (str, optional): Path to the config.yaml file. 
                                        Defaults to the config.yaml in the same directory.
        """
        if config_path is None:
            # Default to config.yaml in the same directory
            config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
        
        # Load configuration
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        # Create API client (will be used by capability implementations)
        self._api_client = PipedriveApiClient()
        
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
    def get_localization(self, params):
        """
        Return localization data for the specified language.
        
        Args:
            params (dict): Dictionary containing:
                - lang: The language code (defaults to 'en')
        """
        return self.localization.get_localization(params.get('lang', 'en'))
    
    # AUTHORIZE CAPABILITY
    def get_authentication_state(self):
        """Get the current authentication state."""
        return self.authorize.get_authentication_state()
        
    def authorize(self, params):
        """
        Authorize with the external system using provided credentials.
        
        Args:
            params (dict): Dictionary containing:
                - credentials: The credentials provided by the user
        
        Returns:
            dict: Authorization result with status
        """
        return self.authorize.authorize(params.get('credentials'))
    
    # ENTITY CAPABILITY
    def get_entities(self):
        """
        Return all available entities for this integration.
        
        Returns:
            list: Array of entity definitions
        """
        return self.entity.get_entities()
    
    def get_entity_schema(self, params):
        """
        Return the schema for a specific entity type (and ID if needed).
        
        Args:
            params (dict): Dictionary containing:
                - entity_type: The entity type
                - entity_id: Optional entity ID for subtypes
            
        Returns:
            dict: JSON Schema definition of the entity
        """
        return self.entity.get_entity_schema(params)
    
    # OBJECT CAPABILITY
    def get_objects(self, params):
        """
        Retrieve a list of available objects for a specific entity type.
        
        Args:
            params (dict): Dictionary containing:
                - entity_type: The type of entity to get objects for
                - entity_id: Optional entity ID for subtypes
            
        Returns:
            list: Array of objects with id and name
        """
        return self.object.get_objects(params)
    
    def get_object_data(self, params):
        """
        Retrieve the complete data for a specific object.
        
        Args:
            params (dict): Dictionary containing:
                - entity_type: The type of entity
                - entity_id: Optional entity ID for subtypes
                - object_id: The ID of the specific object to retrieve
            
        Returns:
            dict: Complete object data with all fields and values
        """
        return self.object.get_object(params)
    
    # ACTION CAPABILITY
    def get_actions(self, params):
        """
        Return all available actions for this integration.
        
        Args:
            params (dict): Dictionary containing:
                - entity_type: Optional entity type to filter actions
        
        Returns:
            list: Array of action definitions with compatible entities
        """
        return self.action.get_actions(params.get('entity_type'))