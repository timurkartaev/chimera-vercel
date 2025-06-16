from apps.connectors.base.capability import BaseCapability
from apps.connectors.base.loader import load_capability_class
from types import MappingProxyType
from typing import Any, List, Dict, Type, get_type_hints
from apps.connectors.base.capabilities import BaseAuthorizeCapability

MissingDependency = object()


def get_capability_class_dependencies(
    capability_class: Type["BaseCapability"],
    connector_context: MappingProxyType[str, Any],
) -> List[Any]:  # You’re returning instances, not types
    import inspect
    import sys

    init_sig = inspect.signature(capability_class.__init__)
    annotations = get_type_hints(
        capability_class.__init__,
        globalns=vars(sys.modules[capability_class.__module__]),
    )
    params = {
        name: param for name, param in init_sig.parameters.items() if name != "self"
    }

    injections = {}
    for name, param in params.items():
        expected_type = annotations.get(name, Any)

        if name in connector_context and isinstance(
            connector_context[name], expected_type
        ):
            injections[name] = connector_context[name]
        elif param.default is not inspect.Parameter.empty:
            injections[name] = param.default
        else:
            raise ValueError(
                f"Missing dependency: {name} for capability {capability_class.__name__}"
            )

    return injections


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
