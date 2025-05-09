from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from chimera.integration_connector.core.config import Config

class ConnectorObject(BaseModel):
    """Base class for connector objects."""
    id: str
    type: str
    data: Dict[str, Any]

class ConnectorResult(BaseModel):
    """Base class for connector operation results."""
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None

class BaseConnector(ABC):
    """Base class for all integration connectors."""

    def __init__(self, config: Config):
        self.config = config
        self._auth_token: Optional[str] = None

    @abstractmethod
    async def authorize(self, credentials: Dict[str, Any]) -> ConnectorResult:
        """Authorize with the external system."""
        pass

    @abstractmethod
    async def get_info(self) -> Dict[str, Any]:
        """Get information about the connector."""
        pass

    @abstractmethod
    async def get_entities(self) -> List[str]:
        """Get list of available entities."""
        pass

    @abstractmethod
    async def get_entity_fields(self, entity_type: str) -> Dict[str, str]:
        """Get fields for a specific entity type."""
        pass

    @abstractmethod
    async def get_objects(self, entity_type: str, filters: Optional[Dict[str, Any]] = None) -> List[ConnectorObject]:
        """Get objects of a specific entity type."""
        pass

    @abstractmethod
    async def get_object(self, entity_type: str, object_id: str) -> ConnectorObject:
        """Get a specific object by ID."""
        pass

    @abstractmethod
    async def create_object(self, entity_type: str, data: Dict[str, Any]) -> ConnectorObject:
        """Create a new object."""
        pass

    @abstractmethod
    async def update_object(self, entity_type: str, object_id: str, data: Dict[str, Any]) -> ConnectorObject:
        """Update an existing object."""
        pass

    @abstractmethod
    async def delete_object(self, entity_type: str, object_id: str) -> ConnectorResult:
        """Delete an object."""
        pass

    @abstractmethod
    async def execute_action(self, action_id: str, entity_type: str, object_id: str, data: Dict[str, Any]) -> ConnectorResult:
        """Execute an action on an object."""
        pass 