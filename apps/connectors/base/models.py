from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class IntegrationConnection(BaseModel):
    id: str
    state: str
    last_active_at: Optional[datetime] = None
    disconnected: bool


class Integration(BaseModel):
    id: str
    key: str
    name: str
    logo: Optional[str] = None
    auth_type: Optional[str] = None
    version: Optional[str] = None
    capabilities: Optional[List[str]] = None


class Identity(BaseModel):
    id: str
    name: str


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


class EntityCapabilityConfig(BaseModel):
    entities: List[str]


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
    entity: Optional[List[str]] = Field(default=None, alias="entities")
    # object capability does not require config
    actions: Optional[ActionCapabilityConfig] = None
