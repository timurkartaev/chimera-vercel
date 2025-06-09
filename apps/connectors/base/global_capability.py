from apps.connectors.base.capability import BaseCapability, BaseCapabilityAction
from pydantic import BaseModel
from django.conf import settings


def list_config_dirs():
    return [x for x in settings.CONNECTOR_CONFIGS_DIR.iterdir() if x.is_dir()]


class ListIntegrations(BaseCapabilityAction):
    """
    ListIntegrations is a capability action that lists all integrations available in the connector.
    It retrieves the list of integrations from the connector's API and returns it as a list of dictionaries.
    """

    Input = None  # No input required

    class Output(BaseModel):
        """
        Output model for ListIntegrations action.
        It contains a list of dictionaries representing the integrations.
        """

        integrations: list[dict]

    def execute(self, input_model: None, context: BaseCapability) -> Output:
        return self.Output(
            integrations=[
                {
                    "slug": integration,
                }
                for integration in list_config_dirs()
            ]
        )


class GlobalCapability(BaseCapability):
    """
    GlobalInfoCapability is a capability that provides global information about the connector.
    It is used to retrieve metadata such as the connector's name, version, and description.
    """

    list_integrations = ListIntegrations(
        description="List all integrations available in the connector."
    )
