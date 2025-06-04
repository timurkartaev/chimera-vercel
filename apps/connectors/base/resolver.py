from apps.connectors.factories.connector_factory import get_connector


def resolve_capability_action(connector_name: str, capability: str, action: str):
    connector = get_connector(connector_name)
    capability_instance = connector.get_capability(capability)

    if not hasattr(capability_instance, action):
        raise NotImplementedError(f"{capability} does not implement '{action}'")

    return getattr(capability_instance, action)
