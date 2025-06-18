import json
from pathlib import Path

from connectors.scripts.coherence_checker.api import IntegrationAPI
from connectors.scripts.coherence_checker.constants import CONNECTIONS
from connectors.scripts.coherence_checker.report import MarkdownReport
from connectors.scripts.coherence_checker.schema import SchemaExtractor


class FieldComparer:
    # Opportunity/Deal
    # Company/Account/Organization
    # Person/Contact/Lead

    @staticmethod
    def run():
        connections = FieldComparer.get_connections()
        print("Connections:" + json.dumps(connections, indent=2))
        base_dir = FieldComparer.get_base_dir()
        for connection_name, connection_id in connections.items():
            md_lines = FieldComparer.process_connection(connection_name, connection_id)
            filename = base_dir / f"{connection_name.lower()}.md"
            filename.write_text("\n".join(md_lines))

    @staticmethod
    def get_connections(api=None, connections_dict=None):
        api = api or IntegrationAPI
        connections_dict = connections_dict or CONNECTIONS
        connections = {}
        for connection in api.list_connections():
            print(f"Connection ID: {connection['id']}, Name: {connection['name']}")
            if connection["name"] not in connections_dict:
                continue
            connections[connection["name"]] = connection["id"]
        return connections

    @staticmethod
    def get_base_dir(base_path=None):
        if base_path is not None:
            base_dir = Path(base_path)
        else:
            base_dir = (
                Path(__file__).parent.parent.parent.parent.parent
                / "docs"
                / "fields-differences"
            )
        base_dir.mkdir(parents=True, exist_ok=True)
        return base_dir

    @staticmethod
    def process_connection(
        connection_name,
        connection_id,
        connections_dict=None,
        api=None,
        schema_extractor=None,
        report=None,
    ):
        connections_dict = connections_dict or CONNECTIONS
        api = api or IntegrationAPI
        schema_extractor = schema_extractor or SchemaExtractor
        report = report or MarkdownReport
        collections = connections_dict[connection_name]
        md_lines = [f"# Differences between fields in {connection_name}\n"]
        for data_collection, data_collection_object_id in collections.items():
            print(f"Processing {data_collection} collection for {connection_name}...")
            md_lines.append(f"\n## {data_collection.capitalize()}\n")
            md_lines.extend(
                FieldComparer.process_collection(
                    connection_name,
                    connection_id,
                    data_collection,
                    data_collection_object_id,
                    api=api,
                    schema_extractor=schema_extractor,
                    report=report,
                )
            )
        return md_lines

    @staticmethod
    def process_collection(
        connection_name,
        connection_id,
        data_collection,
        data_collection_object_id,
        api=None,
        schema_extractor=None,
        report=None,
    ):
        api = api or IntegrationAPI
        schema_extractor = schema_extractor or SchemaExtractor
        report = report or MarkdownReport
        data_collection_schema = api.get_data_collection_schema(
            connection_id, data_collection
        )
        crm_object = api.get_object_by_id(
            connection_name.lower().replace(" ", "-"),
            data_collection,
            data_collection_object_id,
        )
        collection_schema_paths = schema_extractor.extract_schema_paths(
            data_collection_schema.get("fieldsSchema")
        )
        crm_object_paths = schema_extractor.extract_object_paths(
            crm_object.get("output", {}).get("fields", [])
        )
        return report.generate_markdown_table(
            collection_schema_paths,
            crm_object_paths,
            data_collection_schema,
            crm_object,
        )
