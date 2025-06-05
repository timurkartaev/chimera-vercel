from apps.connectors.factories.connector_factory import get_connector

resolve_connector = get_connector


def resolve_capability_action(connector_name: str, capability: str, action: str):
    capability_instance = resolve_capability(connector_name, capability)

    if not hasattr(capability_instance, action):
        raise NotImplementedError(f"{capability} does not implement '{action}'")

    return getattr(capability_instance, action)


def resolve_capability(connector_name: str, capability: str):
    """
    Resolve a capability instance for the given connector and capability name.

    :param connector_name: Name of the connector.
    :param capability: Name of the capability to resolve.
    :return: An instance of the requested capability.
    """
    connector = resolve_connector(connector_name)
    return connector.get_capability(capability)
