from apps.connectors.base.models import Integration, IntegrationConnection
from typing import Any
from datetime import datetime


def map_ipaas_to_integration(data: dict[str, Any]) -> Integration:
    return Integration(
        id=data["id"],
        key=data["key"],
        name=data["name"],
        logo=data.get("logoUri"),
        auth_type=data.get("authType"),
        version=data.get("connectorVersion"),
        capabilities=data.get("capabilities", []),
    )


def map_ipaas_to_integration_connection(data: dict[str, Any]) -> IntegrationConnection:
    return IntegrationConnection(
        id=data["id"],
        state=data["state"],
        last_active_at=data.get("lastActiveAt"),
        disconnected=data.get("disconnected", True),
    )
    