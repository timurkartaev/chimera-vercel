from typing import Any
from apps.connectors.ipaas.capabilities.entity import (
    IpaasGetEntitySchema,
    IpaasListEntities,
    ListEntities,
    GetEntitySchema,
)
from apps.connectors.ipaas.capabilities.object import IpaasGetObject, IpaasListObjects


class CreatioObjectMixin:
    def get_params(self, input_data: IpaasListObjects.Input) -> dict[str, Any]:
        params = super().get_params(input_data)
        params["collectionKey"] = input_data.entity_key
        return params

    def get_entity_key(self, input_data: IpaasListObjects.Input) -> str:
        return "object-collection-instances"


class CreatioGetEntitySchema(IpaasGetEntitySchema):
    def get_url(
        self, input_model: "GetEntitySchema.Input", entity_key: str, method: str
    ) -> str:
        url = super().get_url(input_model, entity_key, method)
        return url + f"?collectionKey={input_model.entity_key}"

    def get_url_part_for_entity(self, input_model: "GetEntitySchema.Input") -> str:
        return "object-collection-instances"


class CreatioListEntities(IpaasListEntities):
    def request(self, session, url: str, input_model: ListEntities.Input) -> dict:
        return session.request("POST", url)

    def get_url_part_for_entity(self, input_model: "ListEntities.Input") -> str:
        return "object-collections"

    def get_method(self) -> str:
        return "list"

    def response_to_raw_entities(self, response: dict) -> list[dict]:
        return response.get("records", [])

    def get_key_and_name(self, data: dict) -> tuple[str, str]:
        return data.get("id"), data.get("name")


class CreatioListObjects(CreatioObjectMixin, IpaasListObjects):
    def get_url_part_for_entity(self, input_model: "IpaasListObjects.Input") -> str:
        return "object-collections"


class CreatioGetObject(CreatioObjectMixin, IpaasGetObject):
    def get_url_part_for_entity(self, input_model: "IpaasGetObject.Input") -> str:
        return "object-collection-instances"


entity__get_entity_schema = CreatioGetEntitySchema("Get entity schema for Creatio")
entity__list_entities = CreatioListEntities("List entities for Creatio")

object__list_objects = CreatioListObjects("List objects for Creatio")
object__get_object = CreatioGetObject("Get object for Creatio")
