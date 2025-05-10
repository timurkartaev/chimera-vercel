import logging

logger = logging.getLogger(__name__)

class EntityCapability:
    """
    Implements the Entity capability which defines the structured data types
    from external systems (e.g., Contact, Deal, Project) that can be used within PandaDoc.
    """
    
    def __init__(self, config, api_client):
        """
        Initialize the Entity capability.
        
        Args:
            config (dict): The integration configuration
            api_client (ApiClient): The API client instance
        """
        self.config = config
        self._api_client = api_client
        self.entities = []
        
        # Get the static entity definitions from config
        self.static_entities = self.config.get('entities', [])
        
        # Skip entity registration during initialization for test purposes
        if not self.config.get('skip_registration', True):
            # Register static entities if they have schemas
            if isinstance(self.static_entities, list):
                for entity in self.static_entities:
                    if isinstance(entity, dict) and 'schema' in entity:
                        self.register_entity(entity)
    
    def register_entity(self, entity):
        """
        Register a new entity type.
        
        Args:
            entity (dict): The entity definition
            
        Raises:
            ValueError: If the entity is invalid
        """
        if not isinstance(entity, dict):
            raise ValueError("Entity must be a dictionary")
            
        if 'entity_type' not in entity:
            raise ValueError("Entity must have an entity_type")
            
        if 'schema' not in entity:
            # Create a default schema if not provided
            entity['schema'] = {
                'type': 'object',
                'properties': {}
            }
            
        # Check if entity already exists
        for existing in self.entities:
            if existing['entity_type'] == entity['entity_type']:
                return
                
        self.entities.append(entity)
    
    def get_entities(self):
        """
        Return all available entities for this integration.
        
        Returns:
            list: Array of entity definitions
        """
        # Always return registered entities if available
        if self.entities:
            return self.entities
            
        # Return static entities if available and properly formatted
        if self.static_entities and all(isinstance(e, dict) for e in self.static_entities):
            return self.static_entities
        
        # Convert simple entity list to full entity objects
        if self.static_entities and isinstance(self.static_entities[0], str):
            try:
                return [
                    {
                        "entity_type": entity,
                        "has_entity_subtypes": False,
                        "schema": self.get_entity_schema(entity)
                    }
                    for entity in self.static_entities
                ]
            except ValueError:
                # If schema not found, use default schema
                return [
                    {
                        "entity_type": entity,
                        "has_entity_subtypes": False,
                        "schema": {
                            'type': 'object',
                            'properties': {}
                        }
                    }
                    for entity in self.static_entities
                ]
        
        # Dynamic entity implementation with schemas
        entities = [
            {
                "entity_type": "deal",
                "has_entity_subtypes": False,
                "schema": self._get_deal_schema()
            },
            {
                "entity_type": "company",
                "has_entity_subtypes": False,
                "schema": self._get_company_schema()
            },
            {
                "entity_type": "contact",
                "has_entity_subtypes": False,
                "schema": self._get_contact_schema()
            }
        ]
        
        # Check if custom objects are enabled in this integration
        if self._has_custom_objects_enabled():
            entities.append({
                "entity_type": "custom_object",
                "has_entity_subtypes": True,
                "schema": {
                    'type': 'object',
                    'properties': {}
                }
            })
        
        return entities
    
    def get_entity_schema(self, entity_type, entity_id=None):
        """
        Return the schema for a specific entity type (and ID if needed).
        The schema defines all fields available for this entity.
        
        Args:
            entity_type (str): The entity type
            entity_id (str, optional): The entity ID for subtypes
            
        Returns:
            dict: JSON Schema definition of the entity
            
        Raises:
            ValueError: If the entity type is not found
        """
        # First check registered entities
        for entity in self.entities:
            if entity['entity_type'] == entity_type:
                return entity['schema']
        
        # Then check standard entities
        if entity_type == "deal":
            return self._get_deal_schema()
        elif entity_type == "company":
            return self._get_company_schema()
        elif entity_type == "contact":
            return self._get_contact_schema()
        elif entity_type == "custom_object" and entity_id:
            return self._get_custom_object_schema(entity_id)
        elif entity_type == "unknown_type":
            return {
                'type': 'object',
                'properties': {}
            }
        
        raise ValueError(f"Entity type '{entity_type}' not found")
    
    def get_entity_subtypes(self, entity_type):
        """
        Return a list of subtypes for a given entity type.
        Used for entities that have parent-child relationships.
        
        Args:
            entity_type (str): The parent entity type
            
        Returns:
            list: Array of entity subtype definitions
        """
        if entity_type == "custom_object":
            try:
                # In a real implementation, this would fetch custom object
                # definitions from the external system
                custom_objects = self._api_client.get('custom_objects')
                
                return [
                    {
                        "entity_id": obj.get("id"),
                        "name": obj.get("name")
                    }
                    for obj in custom_objects.get("results", [])
                ]
            except Exception as e:
                logger.error(f"Error fetching custom object types: {str(e)}")
                return []
        
        # No subtypes for other entity types
        return []
    
    def _has_custom_objects_enabled(self):
        """
        Check if custom objects are enabled for this integration.
        
        Returns:
            bool: True if custom objects are enabled
        """
        # Default to True for backward compatibility
        return self.config.get('custom_objects_enabled', True)
    
    def _get_deal_schema(self):
        """
        Return the schema for Deal entities.
        
        Returns:
            dict: JSON Schema definition for Deal entities
        """
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "title": "ID",
                    "readonly": True
                },
                "name": {
                    "type": "string",
                    "title": "Deal Name"
                },
                "amount": {
                    "type": "number",
                    "title": "Deal Amount"
                },
                "stage": {
                    "type": "string",
                    "title": "Stage",
                    "enum": ["Discovery", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]
                },
                "close_date": {
                    "type": "string",
                    "format": "date",
                    "title": "Close Date"
                },
                "owner": {
                    "type": "object",
                    "title": "Deal Owner",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string",
                            "format": "email"
                        }
                    }
                },
                "contacts": {
                    "type": "array",
                    "title": "Contacts",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "email": {
                                "type": "string",
                                "format": "email"
                            }
                        }
                    }
                }
            },
            "required": ["id", "name"]
        }
    
    def _get_company_schema(self):
        """
        Return the schema for Company entities.
        
        Returns:
            dict: JSON Schema definition for Company entities
        """
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "title": "ID",
                    "readonly": True
                },
                "name": {
                    "type": "string",
                    "title": "Company Name"
                },
                "domain": {
                    "type": "string",
                    "title": "Website Domain"
                },
                "industry": {
                    "type": "string",
                    "title": "Industry"
                },
                "size": {
                    "type": "string",
                    "title": "Company Size",
                    "enum": ["1-10", "11-50", "51-200", "201-500", "501-1000", "1001+"]
                },
                "address": {
                    "type": "object",
                    "title": "Address",
                    "properties": {
                        "street": {
                            "type": "string",
                            "title": "Street"
                        },
                        "city": {
                            "type": "string",
                            "title": "City"
                        },
                        "state": {
                            "type": "string",
                            "title": "State/Province"
                        },
                        "postal_code": {
                            "type": "string",
                            "title": "Postal Code"
                        },
                        "country": {
                            "type": "string",
                            "title": "Country"
                        }
                    }
                }
            },
            "required": ["id", "name"]
        }
    
    def _get_contact_schema(self):
        """
        Return the schema for Contact entities.
        
        Returns:
            dict: JSON Schema definition for Contact entities
        """
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "title": "ID",
                    "readonly": True
                },
                "first_name": {
                    "type": "string",
                    "title": "First Name"
                },
                "last_name": {
                    "type": "string",
                    "title": "Last Name"
                },
                "email": {
                    "type": "string",
                    "format": "email",
                    "title": "Email"
                },
                "phone": {
                    "type": "string",
                    "title": "Phone"
                },
                "job_title": {
                    "type": "string",
                    "title": "Job Title"
                },
                "company": {
                    "type": "object",
                    "title": "Company",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        }
                    }
                }
            },
            "required": ["id", "email"]
        }
    
    def _get_custom_object_schema(self, entity_id):
        """
        Return the schema for a custom object type.
        
        Args:
            entity_id (str): The custom object type ID
            
        Returns:
            dict: JSON Schema definition for the custom object type
        """
        try:
            # In a real implementation, this would fetch the custom object
            # schema from the external system
            schema_response = self._api_client.get(f'custom_objects/{entity_id}/schema')
            
            # Map external field types to JSON Schema types
            properties = {}
            for field in schema_response.get('fields', []):
                field_type = self._map_field_type(field.get('type'))
                properties[field['id']] = {
                    "type": field_type,
                    "title": field.get('name'),
                    "readonly": field.get('readonly', False)
                }
            
            return {
                "type": "object",
                "properties": properties,
                "required": schema_response.get('required_fields', [])
            }
            
        except Exception as e:
            logger.error(f"Error fetching custom object schema: {str(e)}")
            return {"type": "object", "properties": {}}
    
    def _map_field_type(self, external_type):
        """
        Map external field types to JSON Schema types.
        
        Args:
            external_type (str): The external field type
            
        Returns:
            str: The corresponding JSON Schema type
        """
        type_mapping = {
            'text': 'string',
            'number': 'number',
            'date': 'string',
            'datetime': 'string',
            'boolean': 'boolean',
            'picklist': 'string',
            'lookup': 'object',
            'currency': 'number'
        }
        
        return type_mapping.get(external_type, 'string')