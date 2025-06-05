# apps/connectors/factories/connector_factory.py

from typing import Any, Dict, Optional
import yaml
from pathlib import Path


from apps.connectors.base.connector import Connector
from apps.connectors.ipaas.connector import IpaasConnector
from apps.connectors.base.connector import ConnectorConfig


CONNECTOR_YAML_PATH = Path(__file__).resolve().parent.parent / "connector_definitions"
CONNECTOR_TYPE_MAP = {
    "ipaas": IpaasConnector,
}


def load_yaml_file(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return None
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")


def get_connector(name: str) -> Connector:
    """
    Load connector YAML config + localization, parse into ConnectorConfig,
    then create and return Connector instance.
    """
    config_path = CONNECTOR_YAML_PATH / name / "config.yaml"
    localization_path = CONNECTOR_YAML_PATH / name / "localization.yaml"

    config_data = load_yaml_file(config_path)
    localization_data = load_yaml_file(localization_path)

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
    # Construct and return Connector domain object
    return connector_backend_cls(ConnectorConfig.parse_obj(config_data))
