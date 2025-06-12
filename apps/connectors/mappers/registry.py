from typing import Any
from apps.connectors.mappers.ipaas_mapper import (
    map_ipaas_to_integration,
    map_ipaas_to_integration_connection,
)

SERVICE_MODEL_MAPPERS = {
    ("ipaas", "integration"): map_ipaas_to_integration,
    ("ipaas", "integration_connection"): map_ipaas_to_integration_connection,
}


def map_to(service: str, model: str, data: dict[str, Any] | None):
    if data is None:
        return None
    try:
        mapper = SERVICE_MODEL_MAPPERS[(service, model)]
    except KeyError:
        raise ValueError(f"No mapper for service '{service}' and model '{model}'")
    return mapper(data)
