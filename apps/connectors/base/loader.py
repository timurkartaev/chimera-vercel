def load_capability_class_from_module(capability_name: str, module_path: str):
    import importlib

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


def load_bound_capability(capability_name: str, connector_type: str):
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
    module_path = f"apps.connectors.{connector_type}.capabilities.{capability_name}"

    return load_capability_class_from_module(capability_name, module_path)


def load_global_capability(capability_name: str):
    """
    Load a global capability class by its name.
    Global capabilities are expected to be in the 'apps.connectors.global.capabilities' module.
    """
    module_path = "apps.connectors.base.global_capability"
    return load_capability_class_from_module(capability_name, module_path)
