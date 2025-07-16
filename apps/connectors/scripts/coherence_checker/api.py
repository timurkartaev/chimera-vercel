import requests

from connectors.views import get_customer_token


class IntegrationAPI:
    @staticmethod
    def list_connections() -> list[dict]:
        url = "https://api.integration.app/connections"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {get_customer_token('')}",
        }
        response = requests.get(url, headers=headers)
        return response.json().get("items", [])

    @staticmethod
    def get_data_collection_schema(connection_id: str, collection_id: str) -> dict:
        url = f"https://api.integration.app/connections/{connection_id}/data/{collection_id}"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {get_customer_token('')}",
        }
        response = requests.get(url, headers=headers)
        return response.json()

    @staticmethod
    def get_object_by_id(
        integration_name: str, collection: str, object_id: str
    ) -> dict:
        url = f"https://api.integration.app/connections/{integration_name}/actions/find-data-records-by-id/run"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {get_customer_token('')}",
        }
        response = requests.post(
            url,
            headers=headers,
            json={"object": {"id": object_id}, "entity": collection},
        )
        return response.json()
