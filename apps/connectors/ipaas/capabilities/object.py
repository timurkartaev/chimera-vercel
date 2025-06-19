from typing import Any, Optional
from apps.connectors.base.models import ConnectorConfig
from apps.connectors.base.utils import to_camel_case
from apps.connectors.ipaas.api.client import IntegrationAppClient
from connectors.base.capabilities import ListObjects, GetObject, BaseObjectCapability

ENDPOINT_TEMPLATE = "connections/{integration_key}/data/{entity_key}/{method}"


class ObjectActionMixin:
    def get_url(self, input_data: ListObjects.Input, method: str) -> str:
        return ENDPOINT_TEMPLATE.format(
            integration_key=input_data.integration_key,
            entity_key=self.get_entity_key(input_data),
            method=method,
        )

    def get_entity_key(self, input_data: ListObjects.Input) -> str:
        return input_data.entity_key

    def get_params(self, input_data: ListObjects.Input) -> dict[str, Any]:
        params = {}
        if input_data.extra_params:
            for k, v in input_data.extra_params.items():
                if isinstance(v, list):
                    params[to_camel_case(k)] = ",".join(v)
                else:
                    params[to_camel_case(k)] = v
        return params


class IpaasListObjects(ListObjects, ObjectActionMixin):
    def execute(
        self, input_data: ListObjects.Input, context: "ObjectCapability"
    ) -> ListObjects.Output:
        with context.client.with_user_context(
            input_data.identity.id, input_data.identity.name
        ) as session:
            payload = self.get_payload(input_data)
            params = self.get_params(input_data)

            response = session.post(
                self.get_url(input_data, "list"), data=payload, params=params
            )
            return ListObjects.Output(
                objects=response["records"],
                next_page=response.get("cursor"),
            )

    def get_payload(self, input_data: ListObjects.Input) -> dict[str, Any]:
        payload = {}
        if input_data.page:
            payload["cursor"] = input_data.page

        return payload


class IpaasGetObject(GetObject, ObjectActionMixin):
    def execute(
        self, input_data: GetObject.Input, context: "ObjectCapability"
    ) -> GetObject.Output:
        with context.client.with_user_context(
            input_data.identity.id, input_data.identity.name
        ) as session:
            response = session.post(
                self.get_url(input_data, "find-by-id"),
                params=self.get_params(input_data),
                data=self.get_payload(input_data),
            )
            return GetObject.Output(
                object=response["record"],
            )

    def get_payload(self, input_data: GetObject.Input) -> dict[str, Any]:
        return {
            "id": input_data.object_id,
        }


class ObjectCapability(BaseObjectCapability):
    list_objects = IpaasListObjects(description="List objects")
    get_object = IpaasGetObject(description="Get object")

    def __init__(
        self,
        client: IntegrationAppClient,
        config: Optional["ConnectorConfig"] = None,
    ):
        self.client = client
        super().__init__(config)
