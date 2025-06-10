from functools import lru_cache
from pathlib import Path
from typing import List
from pydantic import BaseModel
from apps.connectors.base.capability import BaseCapability, BaseCapabilityAction
from apps.connectors.base.models import Integration
from apps.connectors.base.utils import load_yaml_file
from apps.connectors.ipaas.api.client import IntegrationAppClient
from django.conf import settings

from apps.connectors.ipaas.connector_config import ConnectorConfig


class ListIntegrations(BaseCapabilityAction):
    class Input(BaseModel):
        customer_id: str
        customer_name: str

    class Output(BaseModel):
        items: List[Integration]

    def execute(self, input_model: Input, context: "GlobalCapability"):
        integration_names = [
            config.info.slug for config in context.get_integration_configs()
        ]
        with context.integration_app_client.with_user_context(
            input_model.customer_id, input_model.customer_name
        ) as session:
            integrations = session.list_integrations(integration_names)
        return ListIntegrations.Output(items=integrations)


@lru_cache(maxsize=1)
def get_integration_configs():
    configs = {}
    config_dir: Path = settings.INTEGRATION_CONFIGS_DIR

    for config_base_path in config_dir.iterdir():
        file_path = config_base_path / "config.yaml"
        if file_path.suffix in [".yaml", ".yml"] and file_path.is_file():
            config_data = load_yaml_file(file_path)
            configs[config_base_path.stem] = config_data

    return [ConnectorConfig(**config) for config in configs.values()]


class GlobalCapability(BaseCapability):
    list_integrations = ListIntegrations(description="List all integrations")

    def __init__(self):
        self.integration_app_client = IntegrationAppClient()

    def get_integration_configs(self):
        return get_integration_configs()
