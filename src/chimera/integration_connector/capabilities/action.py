import logging

logger = logging.getLogger(__name__)

class ActionCapability:
    """
    Implements the Action capability which enables operations that send data
    from PandaDoc to the external system.
    """
    
    def __init__(self, config, api_client):
        """
        Initialize the Action capability.
        
        Args:
            config (dict): The integration configuration
            api_client (ApiClient): The API client instance
        """
        self.config = config
        self._api_client = api_client
        
        # Get the static action definitions from config
        self.static_actions = self.config.get('actions', [])
    
    def get_actions(self, entity_type=None):
        """
        Return all available actions for this integration.
        
        Args:
            entity_type (str, optional): Filter actions for a specific entity type
        
        Returns:
            list: Array of action definitions with compatible entities
        """
        # Check if we have static action definitions in the config
        if self.static_actions:
            actions = self.static_actions
        else:
            # Dynamic action implementation
            # This would be customized based on your specific requirements
            actions = [
                {
                    "action_id": "update",
                    "entities": ["deal", "company", "contact"]
                },
                {
                    "action_id": "attach_document",
                    "entities": ["deal", "company"]
                },
                {
                    "action_id": "add_history",
                    "entities": ["deal"]
                }
            ]
        
        # Filter actions by entity type if specified
        if entity_type:
            return [action for action in actions if entity_type in action.get("entities", [])]
        
        return actions
    
    def execute_action(self, action_id, entity_type, object_id, params):
        """
        Execute a specific action on an object.
        
        Args:
            action_id (str): The ID of the action to execute
            entity_type (str): The type of entity
            object_id (str): The ID of the object to perform the action on
            params (dict): Parameters required for the action
            
        Returns:
            dict: Result of the action execution
        """
        # Ensure we're authenticated
        auth_state = self._get_authentication_state()
        if auth_state.get("status") != "connected":
            return {"success": False, "error": "Authentication required"}
        
        # Validate that the action is supported for the entity type
        actions = self.get_actions(entity_type)
        action_ids = [action["action_id"] for action in actions]
        
        if action_id not in action_ids:
            return {"success": False, "error": f"Action '{action_id}' not supported for entity type '{entity_type}'"}
        
        # Dispatch to the appropriate action handler
        try:
            if action_id == "update":
                return self._execute_update_action(entity_type, object_id, params)
            elif action_id == "attach_document":
                return self._execute_attach_document_action(entity_type, object_id, params)
            elif action_id == "add_history":
                return self._execute_add_history_action(entity_type, object_id, params)
            else:
                return {"success": False, "error": f"Action '{action_id}' not implemented"}
        except Exception as e:
            logger.error(f"Error executing action {action_id} on {entity_type} {object_id}: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _get_authentication_state(self):
        """
        Get the current authentication state.
        
        Returns:
            dict: Authentication state information
        """
        # This would be implemented to check the current auth state
        # For simplicity, we'll simulate a connected state
        return {"status": "connected"}
    
    def _execute_update_action(self, entity_type, object_id, params):
        """
        Execute an update action on an object.
        
        Args:
            entity_type (str): The type of entity
            object_id (str): The ID of the object
            params (dict): Parameters for the update action
            
        Returns:
            dict: Result of the action execution
        """
        try:
            properties = params.get("properties", {})
            
            if not properties:
                return {"success": False, "error": "No properties provided for update"}
            
            if entity_type == "deal":
                self._api_client.update_deal(object_id, properties)
            elif entity_type == "company":
                self._api_client.update_company(object_id, properties)
            elif entity_type == "contact":
                self._api_client.update_contact(object_id, properties)
            else:
                return {"success": False, "error": f"Entity type '{entity_type}' does not support update action"}
            
            return {
                "success": True,
                "object_id": object_id,
                "updated_properties": list(properties.keys())
            }
        except Exception as e:
            logger.error(f"Error updating {entity_type} {object_id}: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _execute_attach_document_action(self, entity_type, object_id, params):
        """
        Execute an attach document action on an object.
        
        Args:
            entity_type (str): The type of entity
            object_id (str): The ID of the object
            params (dict): Parameters for the attach document action
            
        Returns:
            dict: Result of the action execution
        """
        try:
            document_id = params.get("document_id")
            document_name = params.get("document_name")
            document_url = params.get("document_url")
            
            if not document_id or not document_url:
                return {"success": False, "error": "Missing required document parameters"}
            
            if entity_type in ["deal", "company"]:
                self._api_client.attach_document(
                    entity_type,
                    object_id,
                    document_id,
                    document_name,
                    document_url
                )
                return {"success": True, "object_id": object_id, "document_id": document_id}
            else:
                return {"success": False, "error": f"Entity type '{entity_type}' does not support attach_document action"}
        except Exception as e:
            logger.error(f"Error attaching document to {entity_type} {object_id}: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def _execute_add_history_action(self, entity_type, object_id, params):
        """
        Execute an add history action on an object.
        
        Args:
            entity_type (str): The type of entity
            object_id (str): The ID of the object
            params (dict): Parameters for the add history action
            
        Returns:
            dict: Result of the action execution
        """
        try:
            activity_type = params.get("activity_type")
            document_id = params.get("document_id")
            document_name = params.get("document_name")
            message = params.get("message")
            
            if not activity_type or not document_id:
                return {"success": False, "error": "Missing required activity parameters"}
            
            if entity_type == "deal":
                self._api_client.add_deal_activity(
                    object_id,
                    activity_type,
                    document_id,
                    document_name,
                    message
                )
                return {"success": True, "object_id": object_id, "activity_type": activity_type}
            else:
                return {"success": False, "error": f"Entity type '{entity_type}' does not support add_history action"}
        except Exception as e:
            logger.error(f"Error adding history to {entity_type} {object_id}: {str(e)}")
            return {"success": False, "error": str(e)}