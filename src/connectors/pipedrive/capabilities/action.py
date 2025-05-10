import logging
from ..integration-connector.capabilities.action import ActionCapability

logger = logging.getLogger(__name__)

class PipedriveActionCapability(ActionCapability):
    """
    Pipedrive action capability that extends the base action capability.
    Currently uses all base functionality without modifications.
    """
    pass

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
        
        # Initialize empty actions list for dynamic registration
        self.actions = []
        
        # Get the static action definitions from config
        self.static_actions = self.config.get('actions', [])
        
        # Register static actions if available
        for action in self.static_actions:
            self.register_action(action)
    
    def register_action(self, action):
        """
        Register a new action.
        
        Args:
            action (dict): The action definition containing:
                - action_id (str): Unique identifier for the action
                - entities (list): List of entity types this action supports
                - parameters (dict, optional): Parameters schema for the action
                - handler (callable, optional): Custom handler function for the action
                
        Raises:
            ValueError: If the action definition is invalid
        """
        if not isinstance(action, dict):
            raise ValueError("Action must be a dictionary")
            
        if 'action_id' not in action:
            raise ValueError("Action must have an action_id")
            
        if 'entities' not in action or not isinstance(action['entities'], list):
            raise ValueError("Action must have a list of supported entities")
            
        # Remove any existing action with the same ID
        self.actions = [a for a in self.actions if a['action_id'] != action['action_id']]
        
        # Add the new action
        self.actions.append(action)
    
    def get_actions(self, params=None):
        """
        Return all available actions for this integration.
        
        Args:
            params (dict, optional): Dictionary containing:
                - entity_type: Optional entity type to filter actions
        
        Returns:
            list: Array of action definitions with compatible entities
        """
        # Use registered actions if available
        if self.actions:
            actions = self.actions
        else:
            # Fallback to static actions from config
            actions = self.static_actions
        
        # Filter actions by entity type if specified
        entity_type = params.get('entity_type') if params else None
        if entity_type:
            return [action for action in actions if entity_type in action.get("entities", [])]
        
        return actions
    
    def execute_action(self, params):
        """
        Execute a specific action on an object.
        
        Args:
            params (dict): Dictionary containing:
                - action_id: The ID of the action to execute
                - entity_type: The type of entity
                - object_id: The ID of the object to perform the action on
                - properties: Optional parameters for the action
            
        Returns:
            dict: Result of the action execution
        """
        action_id = params.get('action_id')
        entity_type = params.get('entity_type')
        object_id = params.get('object_id')
        
        if not all([action_id, entity_type, object_id]):
            return {"success": False, "error": "Missing required parameters"}
        
        # Find the action definition
        action = None
        for a in self.actions:
            if a['action_id'] == action_id:
                action = a
                break
        
        if not action:
            return {"success": False, "error": f"Action '{action_id}' not found"}
        
        # Validate that the action is supported for the entity type
        if entity_type not in action.get('entities', []):
            return {"success": False, "error": f"Action '{action_id}' not supported for entity type '{entity_type}'"}
        
        # If the action has a custom handler, use it
        if 'handler' in action and callable(action['handler']):
            return action['handler'](params)
        
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