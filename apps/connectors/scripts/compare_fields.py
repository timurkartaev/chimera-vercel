import json
from pathlib import Path
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
            json={"collection_name": collection, "object_id": object_id},
        )
        return response.json()


class SchemaExtractor:
    @staticmethod
    def extract_schema_paths(schema, prefix=""):
        paths = set()
        if not schema:
            return paths
        schema_type = schema.get("type")
        if schema_type == "object" and "properties" in schema:
            if prefix:
                paths.add(prefix)  # Add the object field itself
            for prop, prop_schema in schema["properties"].items():
                full_path = f"{prefix}.{prop}" if prefix else prop
                paths |= SchemaExtractor.extract_schema_paths(prop_schema, full_path)
        elif schema_type == "array" and "items" in schema:
            array_path = f"{prefix}" if prefix else ""  # Add the array field itself
            if array_path:
                paths.add(array_path)
            item_path = f"{prefix}[]" if prefix else "[]"
            paths.add(item_path)  # Add the array items path
            paths |= SchemaExtractor.extract_schema_paths(schema["items"], item_path)
        else:
            if prefix:
                paths.add(prefix)
        return paths

    @staticmethod
    def extract_object_paths(obj, prefix=""):
        paths = set()
        if isinstance(obj, dict):
            if prefix:
                paths.add(prefix)  # Add the object field itself
            for k, v in obj.items():
                full_path = f"{prefix}.{k}" if prefix else k
                if isinstance(v, dict):
                    paths.add(full_path)  # Add the object field itself
                    paths |= SchemaExtractor.extract_object_paths(v, full_path)
                elif isinstance(v, list):
                    paths.add(full_path)  # Add the array field itself
                    if v:
                        item_path = f"{full_path}[]"
                        paths.add(item_path)
                        if isinstance(v[0], dict):
                            paths |= SchemaExtractor.extract_object_paths(
                                v[0], item_path
                            )
                    else:
                        # If the list is empty, add the array field and field[] as null
                        item_path = f"{full_path}[]"
                        paths.add(item_path)
                else:
                    paths.add(full_path)
        elif isinstance(obj, list):
            if prefix:
                if obj:
                    paths.add(prefix)
                    item_path = f"{prefix}[]" if prefix else "[]"
                    paths.add(item_path)
                    if isinstance(obj[0], dict):
                        paths |= SchemaExtractor.extract_object_paths(obj[0], item_path)
                else:
                    paths.add(prefix)
                    item_path = f"{prefix}[]" if prefix else "[]"
                    paths.add(item_path)
        else:
            if prefix:
                paths.add(prefix)
        return paths


class SchemaHelper:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def get_reference_records_from_schema(schema, path):
        parts = path.replace("[]", ".items").split(".")
        node = schema
        for part in parts:
            if part == "items":
                node = node.get("items", {})
            elif "properties" in node:
                node = node["properties"].get(part, {})
            else:
                node = {}
        ref = node.get("referenceRecords")
        if ref and isinstance(ref, list):
            # Format as comma-separated quoted names
            return ", ".join(
                f'`{item.get("name")}`' for item in ref if item.get("name") is not None
            )
        return ""

    @staticmethod
    def get_reference_collection_from_schema(schema, path):
        parts = path.replace("[]", ".items").split(".")
        node = schema
        for part in parts:
            if part == "items":
                node = node.get("items", {})
            elif "properties" in node:
                node = node["properties"].get(part, {})
            else:
                node = {}
        ref_coll = node.get("referenceCollection")
        if ref_coll and isinstance(ref_coll, dict):
            return ref_coll.get("key", "")
        return ""

    @staticmethod
    def get_readonly_from_schema(schema, path):
        parts = path.replace("[]", ".items").split(".")
        node = schema
        for part in parts:
            if part == "items":
                node = node.get("items", {})
            elif "properties" in node:
                node = node["properties"].get(part, {})
            else:
                node = {}
        return node.get("readOnly", None)

    @staticmethod
    def get_required_fields(data_collection_schema):
        # Returns a set of required field paths from data_collection_schema['create']['requiredFields']
        required = data_collection_schema.get("create", {}).get("requiredFields", [])
        return set(required)


class MarkdownReport:
    @staticmethod
    def generate_markdown_table(
        collection_schema_paths, crm_object_paths, data_collection_schema, crm_object
    ):
        schema_fields = sorted(collection_schema_paths)
        object_fields = sorted(crm_object_paths)
        schema_fields_set = set(schema_fields)
        object_fields_set = set(object_fields)
        aligned = []
        used_schema = set()
        used_object = set()
        required_fields = SchemaHelper.get_required_fields(data_collection_schema)
        for field in schema_fields:
            readonly = SchemaHelper.get_readonly_from_schema(
                data_collection_schema.get("fieldsSchema", {}), field
            )
            if readonly is True:
                readonly_str = "true"
            elif readonly is False:
                readonly_str = "false"
            else:
                readonly_str = ""
            # Mark required fields with *
            display_field = f"*{field}" if field in required_fields else field
            if field in object_fields_set:
                title = SchemaHelper.get_title_from_schema(
                    data_collection_schema.get("fieldsSchema", {}), field
                )
                dtype_schema = SchemaHelper.get_type_from_schema(
                    data_collection_schema.get("fieldsSchema", {}), field
                )
                dtype_object = SchemaHelper.get_type_from_object(
                    crm_object["output"]["fields"], field
                )
                possible_values = SchemaHelper.get_reference_records_from_schema(
                    data_collection_schema.get("fieldsSchema", {}), field
                )
                reference_collection = (
                    SchemaHelper.get_reference_collection_from_schema(
                        data_collection_schema.get("fieldsSchema", {}), field
                    )
                )
                aligned.append(
                    (
                        title,
                        display_field,
                        dtype_schema,
                        readonly_str,
                        field,
                        dtype_object,
                        possible_values,
                        reference_collection,
                    )
                )
                used_schema.add(field)
                used_object.add(field)
        for field in schema_fields:
            if field not in used_schema:
                readonly = SchemaHelper.get_readonly_from_schema(
                    data_collection_schema.get("fieldsSchema", {}), field
                )
                if readonly is True:
                    readonly_str = "true"
                elif readonly is False:
                    readonly_str = "false"
                else:
                    readonly_str = ""
                display_field = f"*{field}" if field in required_fields else field
                title = SchemaHelper.get_title_from_schema(
                    data_collection_schema.get("fieldsSchema", {}), field
                )
                dtype_schema = SchemaHelper.get_type_from_schema(
                    data_collection_schema.get("fieldsSchema", {}), field
                )
                possible_values = SchemaHelper.get_reference_records_from_schema(
                    data_collection_schema.get("fieldsSchema", {}), field
                )
                reference_collection = (
                    SchemaHelper.get_reference_collection_from_schema(
                        data_collection_schema.get("fieldsSchema", {}), field
                    )
                )
                marked_field = f"<span style='color:red'>***{display_field}***</span>"
                aligned.append(
                    (
                        title,
                        marked_field,
                        dtype_schema,
                        readonly_str,
                        "",
                        "",
                        possible_values,
                        reference_collection,
                    )
                )
                used_schema.add(field)
        for field in object_fields:
            if field not in used_object:
                aligned.append(
                    (
                        "",
                        "",
                        "",
                        "",
                        field,
                        SchemaHelper.get_type_from_object(
                            crm_object["output"]["fields"], field
                        ),
                        "",
                        "",
                    )
                )
                used_object.add(field)
        md_lines = [
            "| Entity Schema Title | Entity Schema Fields | Entity Schema Types | Readonly | Possible Values | Reference Collection | Find By ID Object Fields | Find By ID Types |",
            "|---------------------|----------------------|---------------------|----------|-----------------|----------------------|--------------------------|------------------|",
        ]
        for (
            title,
            left,
            left_type,
            readonly_str,
            right,
            right_type,
            possible_values,
            reference_collection,
        ) in aligned:
            md_lines.append(
                f"| {title or ''} | {left or ''} | {left_type or ''} | {readonly_str or ''} | {possible_values or ''} | {reference_collection or ''} | {right or ''} | {right_type or ''} |"
            )
        return md_lines


class FieldComparer:
    CONNECTIONS = {
        "ActiveCampaign": {
            "deals": "1",
            "contacts": "2",
            "accounts": "1",
        },
        "Close": {
            "opportunity": "oppo_nbV15NALNPtNFPTLOp8gXG5BFT7f8xUE4NeuQ4xoz2l",
            "lead": "lead_HcmG4cyICfAIu1J0sRziNKe63cbNaifOxZZ0PppgksW",
            "contact": "cont_Ga5TgqZ8RIEuhxrhIn0lnULpfpjzWoqoi5R8YG6JVR4",
        },
        "Copper": {
            "opportunities": "15786303",
            "companies": "42499725",
            "leads": "56196888",
        },
        "HubSpot": {
            "deals": "6021835189",
            "contacts": "121593429805",
            "companies": "31115737391",
        },
        "Pipedrive": {
            "deals": "1",
            "persons": "1",
            "organizations": "1",
        },
        "Salesforce": {
            "opportunities": "006gK000001UgviQAC",
            "leads": "00QgK000001WvFWUA0",
            "accounts": "001gK000004nk17QAA",
        },
        "SugarCRM": {
            "opportunities": "db3f6530-30dc-11f0-9285-fb295c038a96",
            "accounts": "d76d391a-30cc-11f0-a99c-1d1bbea39a2d",
            "contacts": "593db44a-30cf-11f0-8746-4f8477825d38",
        },
    }

    @staticmethod
    def run():
        connections = {}
        for connection in IntegrationAPI.list_connections():
            print(f"Connection ID: {connection['id']}, Name: {connection['name']}")
            if connection["name"] not in FieldComparer.CONNECTIONS:
                continue
            connections[connection["name"]] = connection["id"]
        print("Connections:" + json.dumps(connections, indent=2))
        base_dir = (
            Path(__file__).parent.parent.parent.parent / "docs" / "fields-differences"
        )
        base_dir.mkdir(parents=True, exist_ok=True)
        for connection_name, connection_id in connections.items():
            collections = FieldComparer.CONNECTIONS[connection_name]
            md_lines = [f"# Differences between fields in {connection_name}.io\n"]
            for data_collection, data_collection_object_id in collections.items():
                print(
                    f"Processing {data_collection} collection for {connection_name}..."
                )
                md_lines.append(f"\n## {data_collection.capitalize()}\n")
                data_collection_schema = IntegrationAPI.get_data_collection_schema(
                    connection_id, data_collection
                )
                crm_object = IntegrationAPI.get_object_by_id(
                    connection_name.lower(), data_collection, data_collection_object_id
                )
                collection_schema_paths = SchemaExtractor.extract_schema_paths(
                    data_collection_schema.get("fieldsSchema")
                )
                crm_object_paths = SchemaExtractor.extract_object_paths(
                    crm_object["output"]["fields"]
                )
                md_lines.extend(
                    MarkdownReport.generate_markdown_table(
                        collection_schema_paths,
                        crm_object_paths,
                        data_collection_schema,
                        crm_object,
                    )
                )
            filename = base_dir / f"{connection_name.lower()}.md"
            filename.write_text("\n".join(md_lines))


if __name__ == "__main__":
    # print(get_customer_token(""))
    FieldComparer.run()
