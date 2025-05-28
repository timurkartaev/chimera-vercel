from pathlib import Path
from typing import Dict

from apps.connectors.ipaas.connector import IntegrationConnector


# Should be inherited from an Abstract class
class IPaaSConnectorFactory:

    def __init__(self):
        self._configs = self._discover_connectors()

    def _discover_connectors(self) -> Dict[str, str]:
        """Discover available connector configurations."""
        config_path = self._get_config_path()
        
        # Check if configs directory exists
        if not config_path.exists():
            raise FileNotFoundError(f"Config directory not found: {config_path}")
        
        # Store full paths instead of just filenames
        configs = {
            f.stem: str(f.resolve())
            for f in config_path.iterdir()
            if f.is_file()
        }
        return configs

    def create_integration_connector(self, connector_name: str) -> IntegrationConnector:
        """Create an integration connector for the specified connector name."""
        config_path = self._configs.get(connector_name)
        
        if config_path is None:
            available = list(self._configs.keys())
            raise ValueError(f"Connector '{connector_name}' not found. Available: {available}")

        return IntegrationConnector(config_path)

    def _get_config_path(self) -> Path:
        # TODO: could be a classmethod or a staticmethod
        """Get the path to the configs directory."""
        return (Path(__file__).parent / 'configs').resolve()

    def get_discovered_connectors(self) -> list[str]:
        """Get list of discovered connector configuration names."""
        return list(self._configs.keys())
