from typing import Any, Dict

from apps.connectors.ipaas.connector_config import ConnectorConfig
from apps.connectors.ipaas.api.client import IntegrationAppClient
from apps.connectors.base.connector import Connector


class IpaasConnector(Connector):
    def __init__(self, config: ConnectorConfig):
        self.client = IntegrationAppClient()
        super().__init__(config)

    @property
    def connector_context(self) -> Dict[str, Any]:
        """Return the context for this connector, including the client."""
        return {
            "client": self.client,
        }
