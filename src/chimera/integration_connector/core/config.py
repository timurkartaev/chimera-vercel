from typing import Dict, List, Optional
from pydantic import BaseModel, HttpUrl

class Info(BaseModel):
    """Basic metadata that identifies and visually represents the integration."""
    logo: HttpUrl
    name: str
    categories: List[str]
    website: HttpUrl
    support_email: str
    version: str
    developer: str
    description: Optional[str] = None
    video_uri: Optional[HttpUrl] = None
    overview: Optional[str] = None

class OAuth2Config(BaseModel):
    """OAuth2 configuration."""
    client_id: str
    client_secret: str
    auth_uri: HttpUrl
    token_uri: HttpUrl
    scopes: List[str]

class Authentication(BaseModel):
    """Authentication configuration."""
    auth_method: str  # 'oauth2' or 'credentials'
    oauth2: Optional[OAuth2Config] = None

class Entity(BaseModel):
    """Entity configuration."""
    entity_type: str
    display_name: Optional[str] = None
    description: Optional[str] = None
    fields: Optional[Dict[str, str]] = None

class Action(BaseModel):
    """Action configuration."""
    action_id: str
    entities: List[str]
    display_name: Optional[str] = None
    description: Optional[str] = None

class Config(BaseModel):
    """Main configuration model."""
    info: Info
    authentication: Authentication
    entities: List[Entity]
    actions: List[Action]
    localization: Optional[Dict[str, Dict[str, str]]] = None 