from apps.connectors.ipaas.connector_config import ConnectorConfig


class ApiClient:

    def __init__(self, config: ConnectorConfig):
        self.config = config