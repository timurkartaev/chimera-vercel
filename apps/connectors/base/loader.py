import importlib

_BACKEND_TO_CAPABILITIES = {
    "ipaas": "ipaas.capabilities",
}
APPS_MODULE_PATH = "apps.connectors"
BACKEND_TO_CAPABILITIES = {
    key: f"{APPS_MODULE_PATH}.{value}"
    for key, value in _BACKEND_TO_CAPABILITIES.items()
}


def load_capability_class_from_module(module_path: str, capability_name: str):
    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        raise ImportError(f"Capability module '{module_path}' not found.")

    # Compose class name: e.g. "auth" -> "AuthCapability"
    class_name = capability_name.capitalize() + "Capability"

    capability_class = getattr(module, class_name, None)
    if capability_class is None:
        raise ImportError(
            f"Capability class '{class_name}' not found in module '{module_path}'."
        )

    return capability_class


def load_capability_class(capability_name: str, connector_type: str):
    """
    Dynamically import and return the capability class for the given
    capability and connector type.

    Expected module path pattern:
        apps.connectors.<connector_type>.capabilities.<capability_name>

    Class name pattern:
        Capitalized capability name + 'Capability'
        e.g. 'AuthCapability', 'SearchCapability'
    """

    # Compose module path
    module_path = f"{APPS_MODULE_PATH}.{connector_type}.capabilities.{capability_name}"

    return load_capability_class_from_module(module_path, capability_name)


def load_global_capability_class(capability_name: str = "global"):
    module_path = f"{APPS_MODULE_PATH}.base.global_capability"
    return load_capability_class_from_module(module_path, capability_name)


def load_capability_classes(capability_name: str):
    capability_classes = {}
    for backend, capabilities_folder in BACKEND_TO_CAPABILITIES.items():
        capability_classes[backend] = load_capability_class_from_module(
            f"{capabilities_folder}.{capability_name}", capability_name
        )
    return capability_classes


def load_integration_overrides(integration_name: str):
    """
    Dynamically load overrides for a specific integration.
    
    Expected module path pattern:
        apps.connectors.connector_definitions.<integration_name>.overrides
    """
    try:
        module_path = f"{APPS_MODULE_PATH}.connector_definitions.{integration_name}.overrides"
        return importlib.import_module(module_path)
    except ModuleNotFoundError:
        # No overrides found for this integration
        return None