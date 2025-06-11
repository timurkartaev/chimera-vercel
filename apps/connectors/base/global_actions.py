from apps.connectors.base.loader import load_capability_classes


def list_integrations(customer_id: str, customer_name: str):
    capability_classes = load_capability_classes("info")
    integrations = []
    for capability_class in capability_classes.values():
        integrations.extend(
            capability_class()
            .list_integrations(
                dict(
                    customer_id=customer_id,
                    customer_name=customer_name,
                )
            )
            .get("integrations", [])
        )
    return {"items": integrations}
