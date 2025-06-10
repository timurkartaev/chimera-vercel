import json
from pathlib import Path

import requests

from connectors.views import get_customer_token


def list_connections() -> list[dict]:
    url = "https://api.integration.app/connections"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token('')}",
    }
    response = requests.get(url, headers=headers)
    return response.json().get("items", [])


def get_data_collection_schema(connection_id: str, collection_id: str) -> dict:
    url = (
        f"https://api.integration.app/connections/{connection_id}/data/{collection_id}"
    )

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_customer_token('')}",
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_object_by_id(integration_name: str, collection: str, object_id: str) -> dict:
    url = f"https://api.integration.app/connections/{integration_name}/actions/find-data-records-by-id/run"

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_customer_token('')}",
    }
    response = requests.post(
        url,
        headers=headers,
        json={"collection_name": collection, "object_id": object_id},
    )

    return response.json()


CONNECTIONS = {
    "Salesforce": {
        "opportunities": "006gK000001UgviQAC",
        "leads": "00QgK000001WvFWUA0",
        "accounts": "001gK000004nk17QAA",
    },
    "HubSpot": {
        "deals": "6021835189",
        "contacts": "121593429805",
        "companies": "31115737391",
    },
    # "Pipedrive": {
    #     "deals": "1",
    #     "persons": "1",
    #     "organizations": "1",
    # },
    "SugarCRM": {
        "opportunities": "db3f6530-30dc-11f0-9285-fb295c038a96",
        "accounts": "d76d391a-30cc-11f0-a99c-1d1bbea39a2d",
        "contacts": "593db44a-30cf-11f0-8746-4f8477825d38",
    },
    "Copper": {
        "opportunities": "15786303",
        "companies": "42499725",
        "leads": "56196888",
    },
    "Close": {
        "opportunity": "oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l",
        "lead": "lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW",
        "contact": "cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4",
    },
    "ActiveCampaign": {
        "deals": "1",
        "contacts": "2",
        "accounts": "1",
    },
}


def extract_schema_paths(schema, prefix=""):
    paths = set()
    if not schema:
        return paths
    schema_type = schema.get("type")
    if schema_type == "object" and "properties" in schema:
        for prop, prop_schema in schema["properties"].items():
            full_path = f"{prefix}.{prop}" if prefix else prop
            paths |= extract_schema_paths(prop_schema, full_path)
    elif schema_type == "array" and "items" in schema:
        # For arrays, add the array itself and recurse into items
        array_path = f"{prefix}[]" if prefix else "[]"
        paths.add(array_path)
        paths |= extract_schema_paths(schema["items"], array_path)
    else:
        if prefix:
            paths.add(prefix)
    return paths


def extract_object_paths(obj, prefix=""):
    paths = set()
    if not isinstance(obj, dict):
        if prefix:
            paths.add(prefix)
        return paths
    for k, v in obj.items():
        full_path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            paths |= extract_object_paths(v, full_path)
        elif isinstance(v, list):
            # For lists, add the list itself and recurse into first element if possible
            list_path = f"{full_path}[]"
            paths.add(list_path)
            if v and isinstance(v[0], dict):
                paths |= extract_object_paths(v[0], list_path)
        else:
            paths.add(full_path)
    return paths


def main():
    connections = {}
    for connection in list_connections():
        print(f"Connection ID: {connection['id']}, Name: {connection['name']}")
        if connection["name"] not in CONNECTIONS:
            continue
        connections[connection["name"]] = connection["id"]

    print("Connections:" + json.dumps(connections, indent=2))
    base_dir = (
        Path(__file__).parent.parent.parent.parent / "docs" / "fields-differences"
    )
    base_dir.mkdir(parents=True, exist_ok=True)
    for connection_name, connection_id in connections.items():
        collections = CONNECTIONS[connection_name]
        md_lines = [f"# Differences between fields in {connection_name}.io\n"]
        for data_collection, data_collection_object_id in collections.items():
            print(f"Processing {data_collection} collection for {connection_name}...")

            md_lines.append(f"\n## {data_collection.capitalize()}\n")
            data_collection_schema = get_data_collection_schema(
                connection_id, data_collection
            )
            crm_object = get_object_by_id(
                connection_name.lower(), data_collection, data_collection_object_id
            )

            collection_schema_paths = extract_schema_paths(
                data_collection_schema.get("fieldsSchema")
            )
            crm_object_paths = extract_object_paths(crm_object["output"]["fields"])

            # Helper to get type from schema by path
            def get_type_from_schema(schema, path):
                parts = path.replace("[]", ".items").split(".")
                node = schema
                for part in parts:
                    if part == "items":
                        node = node.get("items", {})
                    elif "properties" in node:
                        node = node["properties"].get(part, {})
                    else:
                        node = {}
                return node.get("type", "")

            # Helper to get type from object by path (infer from value)
            def get_type_from_object(obj, path):
                parts = path.replace("[]", "").split(".")
                node = obj
                for part in parts:
                    if isinstance(node, dict) and part in node:
                        node = node[part]
                    elif isinstance(node, list) and node:
                        node = node[0]
                    else:
                        return ""
                if isinstance(node, dict):
                    return "object"
                elif isinstance(node, list):
                    return "array"
                elif node is None:
                    return "null"
                else:
                    return type(node).__name__

            # Helper to get title from schema by path
            def get_title_from_schema(schema, path):
                parts = path.replace("[]", ".items").split(".")
                node = schema
                for part in parts:
                    if part == "items":
                        node = node.get("items", {})
                    elif "properties" in node:
                        node = node["properties"].get(part, {})
                    else:
                        node = {}
                return node.get("title", "")

            # Prepare Markdown table output with sorting and data types for both sides
            schema_fields = sorted(collection_schema_paths)
            object_fields = sorted(crm_object_paths)
            schema_fields_set = set(schema_fields)
            object_fields_set = set(object_fields)
            aligned = []
            used_schema = set()
            used_object = set()
            # First, align fields that are in both (sorted by schema field name)
            for field in schema_fields:
                if field in object_fields_set:
                    title = get_title_from_schema(
                        data_collection_schema.get("fieldsSchema", {}), field
                    )
                    dtype_schema = get_type_from_schema(
                        data_collection_schema.get("fieldsSchema", {}), field
                    )
                    dtype_object = get_type_from_object(
                        crm_object["output"]["fields"], field
                    )
                    aligned.append((title, field, dtype_schema, field, dtype_object))
                    used_schema.add(field)
                    used_object.add(field)
            # Then, add fields only in schema (sorted)
            for field in schema_fields:
                if field not in used_schema:
                    title = get_title_from_schema(
                        data_collection_schema.get("fieldsSchema", {}), field
                    )
                    dtype_schema = get_type_from_schema(
                        data_collection_schema.get("fieldsSchema", {}), field
                    )
                    # Mark missing fields as bold italic and red in Markdown (using HTML <span style="color:red">)
                    marked_field = f"<span style='color:red'>***{field}***</span>"
                    aligned.append((title, marked_field, dtype_schema, "", ""))
                    used_schema.add(field)
            # Then, add fields only in an object (sorted)
            for field in object_fields:
                if field not in used_object:
                    aligned.append(
                        (
                            "",
                            "",
                            "",
                            field,
                            get_type_from_object(crm_object["output"]["fields"], field),
                        )
                    )
                    used_object.add(field)
            md_lines.append(
                "| Entity Schema Title       "
                "| Entity Schema Fields      "
                "| Entity Schema Types       "
                "| Find By ID Object Fields  "
                "| Find By ID Types         |"
            )
            md_lines.append(
                "|---------------------------"
                "|---------------------------"
                "|---------------------------"
                "|---------------------------"
                "|--------------------------|"
            )
            for title, left, left_type, right, right_type in aligned:
                md_lines.append(
                    f"| {title or ''} | {left or ''} | {left_type or ''} | {right or ''} | {right_type or ''} |"
                )
        # Write to file
        filename = base_dir / f"{connection_name.lower()}.md"
        filename.write_text("\n".join(md_lines))


if __name__ == "__main__":
    main()
