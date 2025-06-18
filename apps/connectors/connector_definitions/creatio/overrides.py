from typing import TYPE_CHECKING

from apps.connectors.ipaas.capabilities.entity import (
    IpaasGetEntitySchema,
    IpaasListEntities,
    ListEntities,
    GetEntitySchema,
)


if TYPE_CHECKING:
    from apps.connectors.ipaas.capabilities.entity import (
        EntityCapability,
    )


class EntityGetEntitySchema(IpaasGetEntitySchema):
    def __init__(self, description: str):
        super().__init__(description)

    def get_url(self, input_model: "GetEntitySchema.Input"):
        return "connections/{integration_key}/data/object-collection-instances?collectionKey={entity_key}".format(
            integration_key=input_model.integration_key,
            entity_key=input_model.entity_key,
        )


class EntityListEntities(IpaasListEntities):
    def __init__(self, description: str):
        super().__init__(description)

    def execute(
        self, input_model: "ListEntities.Input", context: "EntityCapability"
    ) -> "ListEntities.Output":
        with context.client.with_user_context(
            input_model.identity.id, input_model.identity.name
        ) as session:
            raw_entities = session.post(self.get_url(input_model)).get("records", [])
            entities = []
            for entity_info in raw_entities:
                entity = {
                    "key": entity_info.get("id"),
                    "name": entity_info.get("name"),
                }

                if entity["key"].lower() in context.config.entity:
                    entities.append(entity)
            return ListEntities.Output(entities=entities)

    def get_url(self, input_model: "ListEntities.Input"):
        return "connections/{integration_key}/data/object-collections/list".format(
            integration_key=input_model.integration_key,
        )


entity__get_entity_schema = EntityGetEntitySchema("Get entity schema for Creatio")
entity__list_entities = EntityListEntities("List entities for Creatio")
