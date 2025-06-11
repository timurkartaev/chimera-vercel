from typing import Optional
from apps.connectors.base.capabilities import (
    BaseInfoCapability,
    GetIntegrationDetails,
    ListIntegrations,
)
from apps.connectors.base.models import ConnectorConfig
from apps.connectors.base.models import Integration
from apps.connectors.ipaas.api.client import (
    IntegrationAppClient,
    get_integration_app_client,
)


class IpaasGetIntegrationDetails(GetIntegrationDetails):
    def execute(
        self, input_model: GetIntegrationDetails.Input, context: "InfoCapability"
    ):
        with context.integration_app_client.with_user_context(
            input_model.customer_id, input_model.customer_name
        ) as session:
            integration = session.get(f"integrations/{input_model.integration_id}")
            return GetIntegrationDetails.Output(integration=Integration(**integration))


class IpaasListIntegrations(ListIntegrations):
    def execute(self, input_model: ListIntegrations.Input, context: "InfoCapability"):
        with context.integration_app_client.with_user_context(
            input_model.customer_id, input_model.customer_name
        ) as session:
            integrations = session.list_integrations(
                self.get_integration_names(input_model.integration_configs)
            )
            return ListIntegrations.Output(integrations=integrations)


class InfoCapability(BaseInfoCapability):
    get_integration_details = IpaasGetIntegrationDetails(description="Get integration details")
    list_integrations = IpaasListIntegrations(description="List integrations")

    def __init__(self, integration_app_client: Optional[IntegrationAppClient] = None):
        self.integration_app_client = (
            integration_app_client or get_integration_app_client()
        )
