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
        connections = {}
        for connection in IntegrationAPI.list_connections():
            print(f"Connection ID: {connection['id']}, Name: {connection['name']}")
            if connection["name"] not in CONNECTIONS:
                continue
            connections[connection["name"]] = connection["id"]
        print("Connections:" + json.dumps(connections, indent=2))
        base_dir = (
            Path(__file__).parent.parent.parent.parent.parent
            / "docs"
            / "fields-differences"
        )
        base_dir.mkdir(parents=True, exist_ok=True)
        for connection_name, connection_id in connections.items():
            collections = CONNECTIONS[connection_name]
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
                    connection_name.lower().replace(" ", "-"),
                    data_collection,
                    data_collection_object_id,
                )
                collection_schema_paths = SchemaExtractor.extract_schema_paths(
                    data_collection_schema.get("fieldsSchema")
                )
                crm_object_paths = SchemaExtractor.extract_object_paths(
                    # crm_object["output"]["fields"]
                    crm_object.get("output", {}).get("fields", [])
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
