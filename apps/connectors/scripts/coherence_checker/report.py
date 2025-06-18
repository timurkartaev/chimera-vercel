import json

from connectors.scripts.coherence_checker.schema import SchemaHelper


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
                        "",  # Diff: Empty (matching)
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
                        "Schema",  # Diff: Schema only (left)
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
                        "FindByID",  # Diff: FindByID only (right)
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
            "| Diff | Entity Schema Title | Schema Field ID | Entity Schema Types | Readonly | Possible Values | Reference Collection | FindByID Field ID | Find By ID Types | Value |",
            "|------|---------------------|-----------------|---------------------|----------|-----------------|----------------------|-------------------|------------------|-------|",
        ]

        def get_field_value(obj, path):
            # Only return value for top-level fields (no dot in path)
            if not path:
                return ""
            parts = []
            for part in path.split("."):
                if part.endswith("[]"):
                    parts.append(part[:-2])
                    parts.append("[]")
                else:
                    parts.append(part)
            node = obj
            for part in parts:
                if part == "[]":
                    if isinstance(node, list):
                        if node:
                            node = node[0]
                        else:
                            return "__empty_array__"
                    else:
                        return ""
                elif isinstance(node, dict) and part in node:
                    node = node[part]
                else:
                    return ""
            if isinstance(node, (dict, list)):
                return json.dumps(node)
            return str(node)

        # Collect all main table field paths to avoid duplication in value rows
        main_table_fields = set()
        for (
            _diff,
            _title,
            left,
            _left_type,
            _readonly_str,
            right,
            _right_type,
            _possible_values,
            _reference_collection,
        ) in aligned:
            if left:
                main_table_fields.add(left)
            if right:
                main_table_fields.add(right)

        def add_value_rows(
            md_lines, obj, path, dtype, readonly_str, skip_main_row=False
        ):
            value = get_field_value(obj, path)
            if dtype == "object" and value and value != "{}":
                # Add value for the object itself only if not skipping main row and not already in main table
                if not skip_main_row and path not in main_table_fields:
                    md_lines.append(
                        f"|  |  | {path} | object | {readonly_str} |  |  | {path} | object | {value} |"
                    )
                try:
                    val_dict = json.loads(value)
                    if isinstance(val_dict, dict):
                        for k, v in val_dict.items():
                            sub_path = f"{path}.{k}" if path else k
                            if sub_path in main_table_fields:
                                continue
                            sub_type = type(v).__name__
                            md_lines.append(
                                f"|  |  | {sub_path} | {sub_type} | {readonly_str} |  |  | {sub_path} | {sub_type} | {json.dumps(v, indent=2) if isinstance(v, (dict, list)) else v} |"
                            )
                except Exception:
                    pass
            elif dtype == "array" and value and value != "[]":
                # Add value for the array itself only if not skipping main row and not already in main table
                if not skip_main_row and path not in main_table_fields:
                    md_lines.append(
                        f"|  |  | {path} | array | {readonly_str} |  |  | {path} | array | {value} |"
                    )
                try:
                    val_list = json.loads(value)
                    if isinstance(val_list, list) and val_list:
                        # Add value for the first item
                        item_path = f"{path}[]"
                        if item_path not in main_table_fields:
                            md_lines.append(
                                f"|  |  | {item_path} | object | {readonly_str} |  |  | {item_path} | object | {json.dumps(val_list[0])} |"
                            )
                        if isinstance(val_list[0], dict):
                            for k, v in val_list[0].items():
                                sub_path = f"{item_path}.{k}"
                                if sub_path in main_table_fields:
                                    continue
                                sub_type = type(v).__name__
                                md_lines.append(
                                    f"|  |  | {sub_path} | {sub_type} | {readonly_str} |  |  | {sub_path} | {sub_type} | {json.dumps(v) if isinstance(v, (dict, list)) else v} |"
                                )
                except Exception:
                    pass
            elif (
                value not in ("", "{}", "[]")
                and not skip_main_row
                and path not in main_table_fields
            ):
                md_lines.append(
                    f"|  |  | {path} | {dtype} | {readonly_str} |  |  | {path} | {dtype} | {value} |"
                )

        for (
            diff,
            title,
            left,
            left_type,
            readonly_str,
            right,
            right_type,
            possible_values,
            reference_collection,
        ) in aligned:
            value = (
                get_field_value(crm_object["output"]["fields"], right) if right else ""
            )
            # If right_type is '__empty_array__', show all possible fields/types from schema in BOTH schema and Find By ID columns
            if right_type == "__empty_array__" and right:
                schema = data_collection_schema.get("fieldsSchema", {})
                parts = right.replace("[]", ".items").split(".")
                node = schema
                for part in parts:
                    if part == "items":
                        node = node.get("items", {})
                    elif "properties" in node:
                        node = node["properties"].get(part, {})
                    else:
                        node = {}
                # Add addresses[] (or similar) as object row if it's an array of objects
                if node.get("type") == "object" and "properties" in node:
                    array_object_row = f"|  |  | {right} | object | {readonly_str} |  |  | {right} | object |  |"
                    md_lines.append(array_object_row)
                    subfields = []
                    for subk, subv in sorted(node["properties"].items()):
                        nested_field = f"{right}[].{subk}".replace("[][].", "[].")
                        nested_type = subv.get("type", "")
                        subfields.append((nested_field, nested_type))
                    for nested_field, nested_type in subfields:
                        md_lines.append(
                            f"|  |  | {nested_field} | {nested_type} | {readonly_str} |  |  | {nested_field} | {nested_type} |  |"
                        )
                elif node.get("type"):
                    md_lines.append(
                        f"|  |  | {right} | {node.get('type')} | {readonly_str} |  |  | {right} | {node.get('type')} |  |"
                    )
                continue  # Skip the main row for the array itself
            # Only add the row if it's not a missing nested field for an empty array
            if not (
                left and left.startswith("<span style='color:red'>***") and "[]" in left
            ):
                md_lines.append(
                    f"| {diff} | {title or ''} | {left or ''} | {left_type or ''} | {readonly_str or ''} | {possible_values or ''} | {reference_collection or ''} | {right or ''} | {right_type or ''} | {value.replace('\r\n', ' ')} |"
                )
            # Add extra value rows for objects and arrays as requested, but skip main row to avoid duplication
            if right and right_type in ("object", "array"):
                add_value_rows(
                    md_lines,
                    crm_object["output"]["fields"],
                    right,
                    right_type,
                    readonly_str,
                    skip_main_row=True,
                )
        return md_lines
