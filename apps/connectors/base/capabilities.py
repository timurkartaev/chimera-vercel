from typing import Any, List, Optional, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict, Field

from apps.connectors.base.capability import BaseCapability, BaseCapabilityAction
from apps.connectors.base.models import Integration
from apps.connectors.base.utils import get_integration_configs
from apps.connectors.base.models import ConnectorConfig


class AuthorizeBegin(BaseCapabilityAction):
    class Input(BaseModel):
        customer_id: str
        customer_name: str

    class Output(BaseModel):
        auth_url: str
        auth_method: str
        auth_params: list[dict[str, Any]]


class AuthorizeFinalize(BaseCapabilityAction):
    class Input(BaseModel):
        code: Optional[str] = None
        state: Optional[str] = None
        error: Optional[str] = None

        model_config = ConfigDict(extra="allow")

    class Output(BaseModel):
        status: str
        redirect_uri: Optional[str] = None
        error_message: Optional[str] = None


class AuthorizeGetAuthFlowStatus(BaseCapabilityAction):
    class Input(BaseModel):
        request_id: str

    class Output(BaseModel):
        status: str
        error_message: Optional[str] = None


class AuthorizeGetConnectionStatus(BaseCapabilityAction):
    class Input(BaseModel):
        integration_id: str

    class Output(BaseModel):
        connected: bool


class BaseAuthorizeCapability(BaseCapability):
    begin: AuthorizeBegin
    finalize: AuthorizeFinalize
    get_auth_flow_status: AuthorizeGetAuthFlowStatus
    get_connection_status: AuthorizeGetConnectionStatus


# Info Capability


class GetIntegrationDetails(BaseCapabilityAction):
    class Input(BaseModel):
        customer_id: str
        customer_name: str

    class Output(BaseModel):
        integration: Integration


class ListIntegrations(BaseCapabilityAction):
    class Input(BaseModel):
        customer_id: str
        customer_name: str
        integration_configs: List["ConnectorConfig"] = Field(
            default_factory=get_integration_configs
        )

    class Output(BaseModel):
        integrations: List[Integration]

    def get_integration_names(
        self, integration_configs: List["ConnectorConfig"]
    ) -> List[str]:
        return [config.info.slug for config in integration_configs]


class BaseInfoCapability(BaseCapability):
    get_integration_details: GetIntegrationDetails
    list_integrations: ListIntegrations

    def __init__(self, config: Optional["ConnectorConfig"] = None):
        self.config = config
