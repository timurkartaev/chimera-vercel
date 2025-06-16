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
    def _traverse_schema(schema, path):
        """
        Traverse a schema using a dot-separated path (with [] for arrays),
        returning the node at the end of the path.
        """
        parts = path.replace("[]", ".items").split(".")
        node = schema
        for part in parts:
            if part == "items":
                node = node.get("items", {})
            elif "properties" in node:
                node = node["properties"].get(part, {})
            else:
                node = {}
        return node

    @staticmethod
    def get_type_from_schema(schema, path):
        node = SchemaHelper._traverse_schema(schema, path)
        return node.get("type", "")

    @staticmethod
    def get_type_from_object(obj, path):
        # Split path into parts, handling [] as array indicators
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
                    return "array" if isinstance(node, list) else ""
            elif isinstance(node, dict) and part in node:
                node = node[part]
            else:
                return ""
        if isinstance(node, dict):
            return "object"
        elif isinstance(node, list):
            return "array"
        elif node is None:
            return "null"
        elif isinstance(node, str):
            return "string"
        elif isinstance(node, bool):
            return "boolean"
        elif isinstance(node, int):
            return "integer"
        elif isinstance(node, float):
            return "number"
        else:
            return type(node).__name__

    @staticmethod
    def get_title_from_schema(schema, path):
        node = SchemaHelper._traverse_schema(schema, path)
        return node.get("title", "")

    @staticmethod
    def get_reference_records_from_schema(schema, path):
        node = SchemaHelper._traverse_schema(schema, path)
        ref = node.get("referenceRecords")
        if ref and isinstance(ref, list):
            return ", ".join(
                f'`{item.get("name")}`' for item in ref if item.get("name") is not None
            )
        return ""

    @staticmethod
    def get_reference_collection_from_schema(schema, path):
        node = SchemaHelper._traverse_schema(schema, path)
        ref_coll = node.get("referenceCollection")
        if ref_coll and isinstance(ref_coll, dict):
            return ref_coll.get("key", "")
        return ""

    @staticmethod
    def get_readonly_from_schema(schema, path):
        node = SchemaHelper._traverse_schema(schema, path)
        return node.get("readOnly", False)

    @staticmethod
    def get_required_fields(data_collection_schema):
        # Returns a set of required field paths from data_collection_schema['create']['requiredFields']
        required = data_collection_schema.get("create", {}).get("requiredFields", [])
        return set(required)
