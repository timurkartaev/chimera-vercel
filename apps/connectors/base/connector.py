from apps.connectors.base.capability import BaseCapability
from apps.connectors.base.loader import load_capability_class
from types import MappingProxyType
from typing import Any, List, Optional, Dict, Type
from pydantic import BaseModel

MissingDependency = object()


def get_capability_class_dependencies(
    capability_class: Type[BaseCapability],
    connector_context: MappingProxyType[str, Any],
) -> List[Type[BaseCapability]]:
    import inspect

    init_sig = inspect.signature(capability_class.__init__)
    params = {
        name: param for name, param in init_sig.parameters.items() if name != "self"
    }
    injectios = {}
    for name, param in params.items():
        if name in connector_context and isinstance(
            connector_context[name], param.annotation
        ):
            injectios[name] = connector_context[name]
        elif param.default is not inspect.Parameter.empty:
            injectios[name] = param.default
        else:
            raise ValueError(
                f"Missing dependency: {name} for capability {capability_class.__name__}"
            )

    return injectios


class Connector:
    def __init__(self, config: "ConnectorConfig"):
        self.config = config
        self.name = config.info.name
        self.type = config.type
        self.capabilities = config.capabilities
        self._capability_instances = self._load_capabilities()

    def _load_capabilities(self) -> dict[str, BaseCapability]:
        result = {}
        for name in self.capabilities:
            cap_cls = load_capability_class(name, self.type)
            result[name] = cap_cls(
                **get_capability_class_dependencies(cap_cls, self.get_connector_context)
            )
        return result

    @property
    def connector_context(self) -> Dict[str, Any]:
        return {}

    @property
    def default_connector_context(self) -> Dict[str, Any]:
        return {"config": self.config}

    def get_connector_context(self) -> MappingProxyType[str, Any]:
        context = {**self.default_connector_context}
        context.update(self.connector_context)
        return MappingProxyType(context)

    def get_capability(self, name: str) -> BaseCapability:
        if name not in self._capability_instances:
            raise ValueError(f"Capability '{name}' not supported by this connector")
        return self._capability_instances[name]


# --- Info Capability ---
class InfoCapabilityConfig(BaseModel):
    name: str
    description: Optional[str] = None
    version: Optional[str] = None
    author: Optional[str] = None
    homepage_url: Optional[str] = None
    # Add more fields as per your actual Info section


# --- Localization Capability ---
class LocalizationEntry(BaseModel):
    key: str
    translations: Dict[str, str]  # e.g., {"en": "Name", "fr": "Nom"}


class LocalizationCapabilityConfig(BaseModel):
    entries: List[LocalizationEntry]


# --- Authorize Capability ---
class AuthMethodConfig(BaseModel):
    method: str  # e.g., "oauth2", "api_key"
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    token_url: Optional[str] = None
    scopes: Optional[List[str]] = None
    # Additional fields depending on method


class AuthorizeCapabilityConfig(BaseModel):
    auth_methods: List[AuthMethodConfig]


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
    type: str
    capabilities: List[str]
    info: Optional[InfoCapabilityConfig] = None
    localization: Optional[LocalizationCapabilityConfig] = None
    authorize: Optional[AuthorizeCapabilityConfig] = None
    entity: Optional[EntityCapabilityConfig] = None
    # object capability does not require config
    actions: Optional[ActionCapabilityConfig] = None
