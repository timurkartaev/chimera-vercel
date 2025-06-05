from apps.connectors.base.capability import BaseCapability
from apps.connectors.base.loader import load_capability_class
from types import MappingProxyType
from typing import Any, List, Optional, Dict, Type
from pydantic import BaseModel, Field
from apps.connectors.base.capability import BaseAuthorizeCapability

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
                f"Missing dependency: {name} for capability {capability_class.__name__} in connector_context {connector_context}"
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
                **get_capability_class_dependencies(
                    cap_cls, self.get_connector_context()
                )
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

    @property
    def authorize(self) -> "BaseAuthorizeCapability":
        return self.get_capability("authorize")

    def authorize__begin(self, customer: Dict[str, Any]):
        """
        Begin the authorization process for a customer.
        This method should be implemented by the specific connector.
        """
        return self.authorize.begin(customer)

    def authorize__finalize(self, query_params: Dict[str, Any]):
        """
        Finalize the authorization process using query parameters.
        This method should be implemented by the specific connector.
        """
        return self.authorize.finalize(query_params)


# --- Info Capability ---
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
