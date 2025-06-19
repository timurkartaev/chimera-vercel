from typing import Any
from apps.connectors.ipaas.capabilities.entity import (
    IpaasGetEntitySchema,
    IpaasListEntities,
)

from apps.connectors.ipaas.capabilities.object import (
    IpaasGetObject,
    IpaasListObjects,
)


class MondayObjectMixin:
    def get_params(self, input_data: IpaasListObjects.Input) -> dict[str, Any]:
        params = super().get_params(input_data)
        params["boardId"] = input_data.entity_key
        return params

    def get_entity_key(self, input_data: IpaasListObjects.Input) -> str:
        return "items"


# ORDER OF BASE CLASSES MATTERS HERE
class MondayListObjects(MondayObjectMixin, IpaasListObjects):
    pass


# ORDER OF BASE CLASSES MATTERS HERE
class MondayGetObject(MondayObjectMixin, IpaasGetObject):
    pass


class MondayListEntities(IpaasListEntities):
    def get_method(self) -> str:
        return "list"

    def get_url_part_for_entity(self, input_model: IpaasListEntities.Input) -> str:
        return "boards"
    
    def request(self, session, url: str, input_model: IpaasListEntities.Input) -> dict:
        return session.request("POST", url)

    def response_to_raw_entities(self, response: dict) -> list[dict]:
        return response.get("records", [])

    def get_key_and_name(self, data: dict) -> tuple[str, str]:
        return data.get("id"), data.get("name")
    
    def filter_func(self, key: str, name: str, config: "ConnectorConfig") -> bool:
        return True


class MondayGetEntitySchema(IpaasGetEntitySchema):
    def get_url(
        self, input_model: "IpaasGetEntitySchema.Input", entity_key: str, method: str
    ) -> str:
        url = super().get_url(input_model, entity_key, method)
        return url + f"?boardId={input_model.entity_key}"

    def get_url_part_for_entity(self, input_model: "IpaasGetEntitySchema.Input") -> str:
        return "items"


object__list_objects = MondayListObjects(description="List objects for Monday")
object__get_object = MondayGetObject(description="Get object for Monday")

entity__list_entities = MondayListEntities(description="List entitties for Monday")
entity__get_entity_schema = MondayGetEntitySchema(description="Get entity schema for Monday")
