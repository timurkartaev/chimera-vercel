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
    import importlib

    # Compose module path
    module_path = f"apps.connectors.{connector_type}.capabilities.{capability_name}"

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
