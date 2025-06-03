from typing import Any
import yaml
from apps.connectors.ipaas.capabilities.authenticate import AuthConfig
from pydantic import ValidationError

from apps.connectors.ipaas import capabilities
from apps.connectors.ipaas.connector_config import ConnectorConfig
from apps.connectors.ipaas.api.client import ApiClient


# TODO: Should be inherited from an abstract class
class IntegrationConnector:

    def __init__(self, config_path: str):
        self.connector_config = self._load_configuration(config_path)
        self.api_client = ApiClient(self.connector_config)
        self._capabilities = self._setup_capabilities()

    def _setup_capabilities(self):
        return {
            'authenticate': capabilities.AuthenticateCapability(self.connector_config, self.api_client),
        }

    def authenticate(self, customer: dict[str, Any]) -> AuthConfig:
        return self._capabilities.get('authenticate').get_authentication_config(customer)
    
    def handle_callback(self, request):
        return self._capabilities.get('authenticate').handle_callback(request)

    def get_connection_state(self):
        pass

    def get_actions(self):
        pass

    def _load_configuration(self, config_path: str) -> ConnectorConfig:
        """Load and validate YAML configuration using Pydantic v2."""
        try:
            # Read YAML file directly
            with open(config_path, 'r', encoding='utf-8') as file:
                yaml_data = yaml.safe_load(file)
            
            if yaml_data is None:
                raise ValueError(f"Empty or invalid YAML file: {config_path}")

            # Validate and parse with Pydantic v2 - using model_validate
            config = ConnectorConfig.model_validate(yaml_data)
            return config
            
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML syntax in {config_path}: {e}")
        except ValidationError as e:
            raise ValueError(f"Configuration validation failed for {config_path}: {e}")
        except Exception as e:
            raise RuntimeError(f"Failed to load configuration from {config_path}: {e}") 