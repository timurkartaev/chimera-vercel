from abc import ABC, abstractmethod
from typing import Any, List, Optional
from pydantic import BaseModel, ConfigDict, Field

from apps.connectors.base.capability import BaseCapability, BaseCapabilityAction
from apps.connectors.base.models import Identity, Integration, IntegrationConnection
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


class AuthorizeGetConnection(BaseCapabilityAction):
    class Input(BaseModel):
        integration_key: str
        identity: Identity

    class Output(BaseModel):
        connection: Optional[IntegrationConnection] = None


class AuthorizeDisconnectConnection(BaseCapabilityAction):
    class Input(BaseModel):
        connection_id: str
        identity: Identity

    class Output(BaseModel):
        # Common statuses for a delete method response are "success" and "error".
        success: bool
        connection: Optional[IntegrationConnection] = None


class BaseAuthorizeCapability(BaseCapability):
    begin: AuthorizeBegin
    finalize: AuthorizeFinalize
    get_auth_flow_status: AuthorizeGetAuthFlowStatus
    get_connection: AuthorizeGetConnection
    disconnect_connection: AuthorizeDisconnectConnection


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
    get_integration: GetIntegrationDetails
    list_integrations: ListIntegrations

    def __init__(self, config: Optional["ConnectorConfig"] = None):
        self.config = config


# Entity Capability


class ListEntities(BaseCapabilityAction):
    class Input(BaseModel):
        integration_key: str
        identity: Identity

    class Output(BaseModel):
        entities: List[dict[str, Any]]


class GetEntitySchema(BaseCapabilityAction):
    class Input(BaseModel):
        integration_key: str
        entity_key: str
        identity: Identity

    class Output(BaseModel):
        schema: dict[str, Any]


class BaseEntityCapability(BaseCapability):
    list_entities: ListEntities
    get_entity_schema: GetEntitySchema


class ListObjects(BaseCapabilityAction):
    class Input(BaseModel):
        integration_key: str
        entity_key: str
        page: Optional[str] = None
        page_size: Optional[int] = None
        extra_params: Optional[dict[str, Any]] = None
        identity: Identity

    class Output(BaseModel):
        objects: List[dict[str, Any]]
        next_page: Optional[str] = None


class GetObject(BaseCapabilityAction):
    class Input(BaseModel):
        integration_key: str
        entity_key: str
        object_id: str
        extra_params: Optional[dict[str, Any]] = None
        identity: Identity

    class Output(BaseModel):
        object: dict[str, Any]


class BaseObjectCapability(BaseCapability):
    list_objects: ListObjects
    get_object: GetObject
