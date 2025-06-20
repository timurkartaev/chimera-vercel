from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Optional
from django.conf import settings
import yaml

from apps.connectors.base.models import ConnectorConfig


def load_yaml_file(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return None
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")


@lru_cache(maxsize=10)
def get_integration_configs(backend: Optional[str] = None):
    configs = {}
    config_dir: Path = settings.INTEGRATION_CONFIGS_DIR

    for config_base_path in config_dir.iterdir():
        file_path = config_base_path / "config.yaml"
        if file_path.suffix in [".yaml", ".yml"] and file_path.is_file():
            config_data = load_yaml_file(file_path)
            if backend is None or config_data.get("type") == backend:
                configs[config_base_path.stem] = config_data

    return {config_name: ConnectorConfig(**config) for config_name, config in configs.items()}


def to_camel_case(s: str) -> str:
    s = s.replace("-", "_")
    parts = s.split("_")
    # Capitalize all parts except the first, then join
    return parts[0] + "".join(word.capitalize() for word in parts[1:])
