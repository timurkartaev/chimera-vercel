import os
import yaml
import importlib
from typing import Optional, Type

class IntegrationConnector:
    """
    Base connector class that provides common functionality for all integrations.
    """
    
    @staticmethod
    def create(slug: str, config_path: Optional[str] = None) -> 'IntegrationConnector':
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
    
    def __init__(self, config_path=None):
        """
        Initialize the connector with configuration and capabilities.
        
        Args:
            config_path (str, optional): Path to the config.yaml file
        """
        if config_path is None:
            # Default to config.yaml in the same directory
            config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
        
        # Load configuration
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        # Initialize capabilities
        self._setup_capabilities()
    
    def _setup_capabilities(self):
        """Set up all capability implementations. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement _setup_capabilities()") 