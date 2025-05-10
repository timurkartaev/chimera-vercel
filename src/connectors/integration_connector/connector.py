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
    Base connector class that manages integration capabilities.
    Capabilities are dynamically loaded based on the integration slug.
    """
    
    _instances: Dict[str, Any] = {}
    
    @classmethod
    def create(cls, slug: str, config_path: Optional[str] = None) -> 'IntegrationConnector':
        """
        Factory method to create a connector instance.
        
        Args:
            slug (str): The connector slug (e.g., 'pipedrive')
            config_path (str, optional): Path to the config.yaml file
        
        Returns:
            IntegrationConnector: An instance of the connector
        """
        # Create a new instance
        instance = cls(config_path)
        instance.slug = slug
        return instance
    
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
        """Set up all capability implementations based on the integration slug."""
        # Define capability mapping
        capability_mapping = {
            'info': InfoCapability,
            'localization': LocalizationCapability,
            'authorize': AuthorizeCapability,
            'entity': EntityCapability,
            'object': ObjectCapability,
            'action': ActionCapability
        }
        
        # Try to load specific implementations for each capability
        for capability_name, base_capability in capability_mapping.items():
            try:
                # Try to import the specific capability implementation
                module_path = f"connectors.{self.slug}.capabilities.{capability_name}"
                specific_capability = importlib.import_module(module_path)
                
                # Get the specific capability class (e.g., PipedriveInfoCapability)
                capability_class_name = f"{self.slug.title()}{capability_name.title()}Capability"
                capability_class = getattr(specific_capability, capability_class_name)
                
                # Initialize the specific capability
                setattr(self, capability_name, capability_class(self.config, self._api_client))
            except (ImportError, AttributeError):
                # Fall back to base capability if specific implementation not found
                setattr(self, capability_name, base_capability(self.config, self._api_client))
    
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