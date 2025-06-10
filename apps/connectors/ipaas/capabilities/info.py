from apps.connectors.base.capability import BaseInfoCapability, GetIntegrationDetails
from apps.connectors.base.models import Integration


class IpaasGetIntegrationDetails(GetIntegrationDetails):
    def execute(
        self, input_model: GetIntegrationDetails.Input, context: "InfoCapability"
    ):
        with context.integration_app_client.with_user_context(
            input_model.customer_id, input_model.customer_name
        ) as session:
            integration = session.get(f"integrations/{input_model.integration_id}")
            return GetIntegrationDetails.Output(integration=Integration(**integration))


class InfoCapability(BaseInfoCapability):
    get_integration_details = GetIntegrationDetails
