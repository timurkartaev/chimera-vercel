from typing import Callable, Optional
from pathlib import Path
from apps.connectors.base.utils import load_yaml_file

from apps.connectors.base.connector import Connector
from apps.connectors.ipaas.connector import IpaasConnector
from apps.connectors.base.connector import ConnectorConfig


CONNECTOR_YAML_PATH = Path(__file__).resolve().parent.parent / "connector_definitions"
CONNECTOR_TYPE_MAP = {
    "ipaas": IpaasConnector,
}

def fallback_config_factory(name: str) -> ConnectorConfig:
    """
    Fallback factory to create a default ConnectorConfig if no config file is found.
    This can be used when a connector does not have a specific configuration file.
    """
    return ConnectorConfig(
        info={"name": name, "description": f"Default config for {name}"},
        type="ipaas",
        capabilities=["authorize"],
    )


def get_connector(
    name: str,
    fallback_config_factory: Optional[
        Callable[[str], ConnectorConfig]
    ] = fallback_config_factory,
) -> Connector:
    """
    Load connector YAML config + localization, parse into ConnectorConfig,
    then create and return Connector instance.
    """
    config_path = CONNECTOR_YAML_PATH / name / "config.yaml"
    localization_path = CONNECTOR_YAML_PATH / name / "localization.yaml"

    config_data = load_yaml_file(config_path)
    localization_data = load_yaml_file(localization_path)

    if not config_data and fallback_config_factory:
        config_data = fallback_config_factory(name).model_dump()

    if not config_data:
        raise ValueError(f"Connector config file not found: {config_path}")

    if localization_data:
        config_data["localization"] = localization_data

    connector_backend = config_data["type"]
    if not connector_backend:
        raise ValueError(f"Connector backend not specified in {config_path}")
    connector_backend_cls = CONNECTOR_TYPE_MAP.get(connector_backend)
    if not connector_backend_cls:
        raise ValueError(
            f"Unknown connector backend '{connector_backend}' in {config_path}"
        )
    return connector_backend_cls(ConnectorConfig.model_validate(config_data))
