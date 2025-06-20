from typing import Optional

from apps.connectors.base.capabilities import (
    BaseEntityCapability,
    GetEntitySchema,
    ListEntities,
)
from apps.connectors.ipaas.api.client import IntegrationAppClient

from apps.connectors.base.models import ConnectorConfig

ENDPOINT_TEMPLATE = "connections/{integration_key}/data/{entity_key}"


def simple_depluralize(word):
    if word.endswith("ies"):
        return word[:-3] + "y"
    elif word.endswith("es") and not word.endswith("ses"):
        return word[:-2]
    elif word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


class EntityActionMixin:
    def simple_depluralize(self, word: str) -> str:
        if word.endswith("ies"):
            return word[:-3] + "y"
        elif word.endswith("es") and not word.endswith("ses"):
            return word[:-2]
        elif word.endswith("s") and not word.endswith("ss"):
            return word[:-1]
        return word

    def get_url(
        self, input_model: ListEntities.Input, entity_key: str, method: str
    ) -> str:
        url = ENDPOINT_TEMPLATE.format(
            integration_key=input_model.integration_key,
            entity_key=entity_key,
        ).rstrip("/")
        if method:
            url += f"/{method}"
        return url

    def get_url_part_for_entity(self, input_model: ListEntities.Input) -> str:
        return input_model.entity_key

    def get_method(self) -> str:
        return ""


class IpaasListEntities(ListEntities, EntityActionMixin):
    def execute(
        self, input_model: ListEntities.Input, context: "EntityCapability"
    ) -> ListEntities.Output:
        with context.client.with_user_context(
            input_model.identity.id, input_model.identity.name
        ) as session:
            response = self.request(session, self.get_url(input_model, self.get_url_part_for_entity(input_model), self.get_method()), input_model)
            raw_entities = self.response_to_raw_entities(response)
            entities = []
            for entity_info in raw_entities:
                key, name = self.get_key_and_name(entity_info)
                if self.filter_func(key, name, context.config):
                    entities.append({"key": key, "name": name})

            return ListEntities.Output(entities=entities)
        
    def request(self, session, url: str, input_model: ListEntities.Input) -> dict:
        return session.request(self.get_http_method(), url)

    def response_to_raw_entities(self, response: dict) -> list[dict]:
        return response

    def get_key_and_name(self, data: dict) -> tuple[str, str]:
        return data.get("key"), data.get("name")

    def filter_func(self, key: str, name: str, config: "ConnectorConfig") -> bool:
        return simple_depluralize(key).lower() in config.entity
    
    def get_http_method(self) -> str:
        return "GET"
    
    def get_url_part_for_entity(self, input_model: ListEntities.Input) -> str:
        return ""


class IpaasGetEntitySchema(GetEntitySchema, EntityActionMixin):
    def execute(
        self, input_model: GetEntitySchema.Input, context: "EntityCapability"
    ) -> GetEntitySchema.Output:
        with context.client.with_user_context(
            input_model.identity.id, input_model.identity.name
        ) as session:
            schema = session.get(
                self.get_url(
                    input_model, self.get_url_part_for_entity(input_model), self.get_method()
                )
            )
            return GetEntitySchema.Output(schema=schema)


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
