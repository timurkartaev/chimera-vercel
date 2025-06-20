from typing import Optional
from apps.connectors.base.capabilities import (
    BaseInfoCapability,
    GetIntegrationDetails,
    ListIntegrations,
)
from apps.connectors.base.models import ConnectorConfig
from apps.connectors.ipaas.api.client import (
    IntegrationAppClient,
    get_integration_app_client,
)
from apps.connectors.mappers.registry import map_to


class IpaasGetIntegrationDetails(GetIntegrationDetails):
    def execute(
        self, input_model: GetIntegrationDetails.Input, context: "InfoCapability"
    ):
        assert context.config
        with context.client.with_user_context(
            input_model.customer_id, input_model.customer_name
        ) as session:
            integration = session.get(f"integrations/{context.config.info.slug}")
            return GetIntegrationDetails.Output(
                integration=map_to(
                    "ipaas",
                    "integration",
                    {**integration, "capabilities": context.config.capabilities},
                )
            )


class IpaasListIntegrations(ListIntegrations):
    def execute(self, input_model: ListIntegrations.Input, context: "InfoCapability"):
        with context.client.with_user_context(
            input_model.customer_id, input_model.customer_name
        ) as session:
            integrations = session.list_integrations(
                self.get_integration_names(input_model.integration_configs)
            )
            return ListIntegrations.Output(
                integrations=[
                    map_to(
                        "ipaas",
                        "integration",
                        {
                            **integration,
                            "capabilities": context.config.capabilities,
                        },
                    )
                    for integration in integrations
                ]
            )


class InfoCapability(BaseInfoCapability):
    get_integration = IpaasGetIntegrationDetails(description="Get integration details")
    list_integrations = IpaasListIntegrations(description="List integrations")

    def __init__(
        self,
        client: Optional[IntegrationAppClient] = None,
        config: Optional[ConnectorConfig] = None,
    ):
        super().__init__(config)
        self.client = client or get_integration_app_client()
