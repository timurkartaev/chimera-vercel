import os
import yaml
import importlib
from typing import Dict, Any, Optional
from .api.client import ApiClient
from .capabilities.info import InfoCapability
from .capabilities.localization import LocalizationCapability
from .capabilities.authorize import AuthorizeCapability
from .capabilities.entity import EntityCapability
from .capabilities.object import ObjectCapability
from .capabilities.action import ActionCapability

class IntegrationConnector:
    """
    Factory class that creates and manages connector instances based on the slug.
    This class acts as a facade that delegates to specialized connector implementations.
    """
    
    _instances: Dict[str, Any] = {}
    
    @classmethod
    def create(cls, slug: str, config_path: Optional[str] = None) -> Any:
        """
        Factory method to create a connector instance based on the slug.
        
        Args:
            slug (str): The connector slug (e.g., 'pipedrive')
            config_path (str, optional): Path to the config.yaml file
        
        Returns:
            IntegrationConnector: An instance of the appropriate connector class
        
        Raises:
            ImportError: If the connector module cannot be imported
            AttributeError: If the connector class cannot be found
        """
        # Convert slug to proper class name (e.g., 'pipedrive' -> 'PipedriveConnector')
        class_name = f"{slug.title()}Connector"
        
        try:
            # Import the connector module
            module = importlib.import_module(f"connectors.{slug}.connector")
            
            # Get the connector class
            connector_class = getattr(module, class_name)
            
            # Create and return an instance
            return connector_class(config_path)
            
        except ImportError as e:
            raise ImportError(f"Could not import connector module for '{slug}': {str(e)}")
        except AttributeError as e:
            raise AttributeError(f"Could not find connector class '{class_name}' in module '{slug}': {str(e)}")
    
    @classmethod
    def get_available_connectors(cls) -> list:
        """
        Get a list of available connector slugs.
        
        Returns:
            list: List of available connector slugs
        """
        connectors_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)))
        return [d for d in os.listdir(connectors_dir) 
                if os.path.isdir(os.path.join(connectors_dir, d)) 
                and not d.startswith('.')]
    
    def __init__(self, config_path=None):
        """
        Initialize the connector with configuration and capabilities.
        
        Args:
            config_path (str, optional): Path to the config.yaml file. 
                                        Defaults to the config.yaml in the same directory.
        """
        if config_path is None:
            # Default to config.yaml in the same directory as this file
            config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
        
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
    
    def get_object(self, params):
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
    
    def execute_action(self, action_id, entity_type, object_id, params):
        """
        Execute a specific action on an object.
        
        Args:
            action_id (str): The ID of the action to execute
            entity_type (str): The type of entity
            object_id (str): The ID of the object
            params (dict): Additional parameters for the action
        
        Returns:
            dict: Result of the action execution
        """
        return self.action.execute_action(action_id, entity_type, object_id, params)