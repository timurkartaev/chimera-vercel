from typing import Optional

from apps.connectors.base.capabilities import (
    BaseEntityCapability,
    GetEntitySchema,
    ListEntities,
)
from apps.connectors.ipaas.api.client import IntegrationAppClient

from apps.connectors.base.models import ConnectorConfig


def simple_depluralize(word):
    if word.endswith("ies"):
        return word[:-3] + "y"
    elif word.endswith("es") and not word.endswith("ses"):
        return word[:-2]
    elif word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


class IpaasListEntities(ListEntities):
    def execute(
        self, input_model: ListEntities.Input, context: "EntityCapability"
    ) -> ListEntities.Output:
        with context.client.with_user_context(
            input_model.identity.id, input_model.identity.name
        ) as session:
            raw_entities = session.get(self.get_url(input_model))
            entities = []
            for entity_info in raw_entities:
                entity = {
                    "key": entity_info.get("key"),
                    "name": entity_info.get("name"),
                }
                if simple_depluralize(entity["key"]).lower() in context.config.entity:
                    entities.append(entity)

            return ListEntities.Output(entities=entities)

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
        return "connections/{integration_key}/data/{entity_key}".format(
            integration_key=input_model.integration_key,
            entity_key=input_model.entity_key,
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
