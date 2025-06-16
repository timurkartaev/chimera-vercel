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
        return "connections/{integration_key}/data/object-collection-instances?collectionKey={entity_name}".format(
            integration_key=input_model.integration_key,
            entity_name=input_model.entity_name,
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
            response = session.post(self.get_url(input_model))
            entities = [
                {"key": record.get("id"), "name": record.get("name")}
                for record in response.get("records", [])
            ]
            return ListEntities.Output(entities=entities)

    def get_url(self, input_model: "ListEntities.Input"):
        return "connections/{integration_key}/data/object-collections/list".format(
            integration_key=input_model.integration_key,
        )


entity__get_entity_schema = EntityGetEntitySchema("Get entity schema for Creatio")
entity__list_entities = EntityListEntities("List entities for Creatio")
