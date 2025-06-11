from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class IntegrationConnection(BaseModel):
    id: str
    state: str  # e.g., 'READY', 'ERROR', etc.
    userId: Optional[str]
    createdAt: datetime
    updatedAt: datetime
    lastActiveAt: Optional[datetime] = None
    disconnected: bool

class Integration(BaseModel):
    id: str
    logoUri: Optional[str] = None
    name: str
    state: str
    authType: Optional[str] = None
    connectorVersion: Optional[str] = None
    dataCollectionsCount: Optional[int] = 0
    operationsCount: Optional[int] = 0
    eventsCount: Optional[int] = 0
    key: str
    hasDocumentation: bool = False
    hasUdm: bool = False
    hasEvents: bool = False
    hasGlobalWebhooks: bool = False
    connection: Optional[IntegrationConnection] = None



# Connector Config Schema
class InfoCapabilityConfig(BaseModel):
    name: str
    slug_: Optional[str] = Field(default=None, alias="slug")
    description: Optional[str] = None
    version: Optional[str] = None
    author: Optional[str] = None
    homepage_url: Optional[str] = None

    @property
    def slug(self) -> str:
        if self.slug_:
            return self.slug_
        return self.name.lower().replace(" ", "-").replace("_", "-").replace(".", "-")


# --- Localization Capability ---
class LocalizationEntry(BaseModel):
    key: str
    translations: Dict[str, str]  # e.g., {"en": "Name", "fr": "Nom"}


class LocalizationCapabilityConfig(BaseModel):
    entries: List[LocalizationEntry]


class AuthorizeCapabilityConfig(BaseModel):
    auth_method: str
    auth_params: Optional[List[Dict[str, Any]]] = None
    oauth2: Optional[Dict[str, Any]] = (
        None  # e.g., {"client_id": "xxx", "redirect_uri": "https://example.com/callback"}
    )


# --- Entity Capability ---
class EntityField(BaseModel):
    name: str
    type: str  # e.g., "string", "number", "date"
    required: Optional[bool] = False
    description: Optional[str] = None
    # Add validations, formats, etc. as needed


class EntitySchema(BaseModel):
    entity_type: str  # e.g., "deal", "contact"
    display_name: Optional[str] = None
    fields: List[EntityField]


class EntityCapabilityConfig(BaseModel):
    entities: List[EntitySchema]


# --- Action Capability ---
class ActionConfig(BaseModel):
    action_id: str
    entities: List[str]


class ActionCapabilityConfig(BaseModel):
    actions: List[ActionConfig]


# --- Root config schema ---
class ConnectorConfig(BaseModel):
    # authorize section could also be loaded from alias  "authentication"
    type: str
    capabilities: List[str]
    info: Optional[InfoCapabilityConfig] = None
    localization: Optional[LocalizationCapabilityConfig] = None
    authorize: Optional[AuthorizeCapabilityConfig] = Field(
        default=None, alias="authentication"
    )
    entity: Optional[EntityCapabilityConfig] = None
    # object capability does not require config
    actions: Optional[ActionCapabilityConfig] = None
