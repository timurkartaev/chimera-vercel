from pydantic import BaseModel, ConfigDict, HttpUrl
from typing import List, Optional


class Info(BaseModel):
    name: str
    slug: str

class OAuth2(BaseModel):
    redirect_url: HttpUrl

class Authentication(BaseModel):
    auth_method: str
    oauth2: Optional[OAuth2] = None

class ConnectorConfig(BaseModel):
    info: Info
    authentication: Optional[Authentication] = None
    capabilities: Optional[List[str]] = None

    model_config = ConfigDict(
        frozen=True
    )

