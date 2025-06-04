from typing import Any, Dict

from apps.connectors.ipaas.connector_config import ConnectorConfig
from apps.connectors.ipaas.api.client import IpaasClient
from apps.connectors.base.connector import Connector


class IpaasConnector(Connector):
    def __init__(self, config: ConnectorConfig):
        super().__init__(config)
        self.client = IpaasClient(config)

    def authorize__begin(self, customer: Dict[str, Any]) -> str:
        return self.authorize.begin(customer)

    def authorize__finalize(self, query_params: Dict[str, Any]) -> dict[str, Any]:
        return self.authorize.finilize(query_params)
