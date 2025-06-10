from pathlib import Path
from typing import Any, Dict, Optional
import yaml


def load_yaml_file(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return None
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")
