from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class IntegrationConnection(BaseModel):
    id: str
    state: str
    lastActiveAt: datetime


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
