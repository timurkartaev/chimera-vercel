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
        
        # Get the static entity definitions from config
        self.static_entities = self.config.get('entities', [])
    
    def get_entities(self):
        """
        Return all available entities for this integration.
        
        Returns:
            list: Array of entity definitions
        """
        # Check if we have static entity definitions in the config
        if self.static_entities:
            # Convert simple entity list to full entity objects
            if isinstance(self.static_entities[0], str):
                return [{"entity_type": entity, "has_entity_subtypes": False} 
                        for entity in self.static_entities]
            # Already in the correct format
            return self.static_entities
        
        # Dynamic entity implementation
        # This would be customized based on your specific requirements
        entities = [
            {"entity_type": "deal", "has_entity_subtypes": False},
            {"entity_type": "company", "has_entity_subtypes": False},
            {"entity_type": "contact", "has_entity_subtypes": False}
        ]
        
        # Check if custom objects are enabled in this integration
        if self._has_custom_objects_enabled():
            entities.append({"entity_type": "custom_object", "has_entity_subtypes": True})
        
        return entities
    
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
    
    def get_entity_schema(self, entity_type, entity_id=None):
        """
        Return the schema for a specific entity type (and ID if needed).
        The schema defines all fields available for this entity.
        
        Args:
            entity_type (str): The entity type
            entity_id (str, optional): The entity ID for subtypes
            
        Returns:
            dict: JSON Schema definition of the entity
        """
        # Standard entity schemas
        if entity_type == "deal":
            return self._get_deal_schema()
        elif entity_type == "company":
            return self._get_company_schema()
        elif entity_type == "contact":
            return self._get_contact_schema()
        elif entity_type == "custom_object" and entity_id:
            return self._get_custom_object_schema(entity_id)
        
        # Default empty schema
        return {"type": "object", "properties": {}}
    
    def _has_custom_objects_enabled(self):
        """
        Check if custom objects are enabled for this integration.
        
        Returns:
            bool: True if custom objects are enabled
        """
        # This would be implemented based on your specific requirements
        # For example, checking a feature flag in the integration configuration
        return True
    
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
        Return the schema for a specific custom object type.
        
        Args:
            entity_id (str): The ID of the custom object type
            
        Returns:
            dict: JSON Schema definition for the custom object type
        """
        try:
            # In a real implementation, this would fetch the custom object
            # schema from the external system
            custom_object_schema = self._api_client.get(f'custom_objects/{entity_id}/schema')
            
            # Transform the API response to a JSON Schema
            # This is a simplified example
            properties = {}
            for field in custom_object_schema.get("fields", []):
                field_type = self._map_field_type(field.get("type"))
                properties[field.get("id")] = {
                    "type": field_type,
                    "title": field.get("name"),
                    "readonly": field.get("readonly", False)
                }
            
            return {
                "type": "object",
                "properties": properties,
                "required": ["id"]
            }
            
        except Exception as e:
            logger.error(f"Error fetching custom object schema: {str(e)}")
            return {"type": "object", "properties": {}}
    
    def _map_field_type(self, external_type):
        """
        Map external system field types to JSON Schema types.
        
        Args:
            external_type (str): Field type from the external system
            
        Returns:
            str: JSON Schema type
        """
        # This mapping would be customized based on the external system
        type_mapping = {
            "text": "string",
            "number": "number",
            "date": "string",  # With format: date
            "datetime": "string",  # With format: date-time
            "boolean": "boolean",
            "picklist": "string",  # With enum
            "lookup": "object",
            "currency": "number"
        }
        
        return type_mapping.get(external_type, "string")