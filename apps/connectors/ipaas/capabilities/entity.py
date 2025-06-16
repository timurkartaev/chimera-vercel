from typing import Optional

from apps.connectors.base.capabilities import (
    BaseEntityCapability,
    GetEntitySchema,
    ListEntities,
)
from apps.connectors.ipaas.api.client import IntegrationAppClient

from apps.connectors.base.models import ConnectorConfig


class IpaasListEntities(ListEntities):
    def execute(
        self, input_model: ListEntities.Input, context: "EntityCapability"
    ) -> ListEntities.Output:
        with context.client.with_user_context(
            input_model.identity.id, input_model.identity.name
        ) as session:
            entities = session.get(self.get_url(input_model))
            return ListEntities.Output(
                entities=[
                    {
                        "key": entity.get("key"),
                        "name": entity.get("name"),
                    }
                    for entity in entities
                ]
            )

    def get_url(self, input_model: ListEntities.Input):
        return "connections/{integration_key}/data".format(
            integration_key=input_model.integration_key,
        )


class IpaasGetEntitySchema(GetEntitySchema):
    def execute(
        self, input_model: GetEntitySchema.Input, context: "EntityCapability"
    ) -> GetEntitySchema.Output:
        with context.client.with_user_context(
            input_model.identity.id, input_model.identity.name
        ) as session:
            schema = session.get(self.get_url(input_model))
            return GetEntitySchema.Output(schema=schema)

    def get_url(self, input_model: GetEntitySchema.Input):
        return "connections/{integration_key}/data/{entity_name}".format(
            integration_key=input_model.integration_key,
            entity_name=input_model.entity_name,
        )


class EntityCapability(BaseEntityCapability):
    list_entities = IpaasListEntities(description="List entities")
    get_entity_schema = IpaasGetEntitySchema(description="Get entity schema")

    def __init__(
        self,
        client: IntegrationAppClient,
        config: Optional["ConnectorConfig"] = None,
    ):
        self.client = client
        super().__init__(config)
