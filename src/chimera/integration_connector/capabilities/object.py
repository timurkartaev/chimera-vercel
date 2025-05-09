import logging

logger = logging.getLogger(__name__)

class ObjectCapability:
    """
    Implements the Object capability which provides access to actual instances
    of Entities from the external system.
    """
    
    def __init__(self, config, api_client):
        """
        Initialize the Object capability.
        
        Args:
            config (dict): The integration configuration
            api_client (ApiClient): The API client instance
        """
        self.config = config
        self._api_client = api_client
    
    def get_objects(self, entity_type, entity_id=None):
        """
        Retrieve a list of available objects for a specific entity type.
        
        Args:
            entity_type (str): The type of entity to get objects for
            entity_id (str, optional): The entity ID for subtypes
            
        Returns:
            list: Array of objects with id and name
        """
        # Ensure we're authenticated
        auth_state = self._get_authentication_state()
        if auth_state.get("status") != "connected":
            logger.error("Authentication required to fetch objects")
            return []
        
        try:
            # Dispatch to the appropriate method based on entity type
            if entity_type == "deal":
                return self._get_deals()
            elif entity_type == "company":
                return self._get_companies()
            elif entity_type == "contact":
                return self._get_contacts()
            elif entity_type == "custom_object" and entity_id:
                return self._get_custom_objects(entity_id)
            else:
                logger.warning(f"Unsupported entity type: {entity_type}")
                return []
                
        except Exception as e:
            logger.error(f"Error fetching objects for entity type {entity_type}: {str(e)}")
            return []
    
    def get_object_data(self, entity_type, entity_id, object_id):
        """
        Retrieve the complete data for a specific object.
        
        Args:
            entity_type (str): The type of entity
            entity_id (str, optional): The entity ID for subtypes
            object_id (str): The ID of the specific object to retrieve
            
        Returns:
            dict: Complete object data with all fields and values
        """
        # Ensure we're authenticated
        auth_state = self._get_authentication_state()
        if auth_state.get("status") != "connected":
            logger.error("Authentication required to fetch object data")
            return {}
        
        try:
            # Dispatch to the appropriate method based on entity type
            if entity_type == "deal":
                return self._get_deal_data(object_id)
            elif entity_type == "company":
                return self._get_company_data(object_id)
            elif entity_type == "contact":
                return self._get_contact_data(object_id)
            elif entity_type == "custom_object" and entity_id:
                return self._get_custom_object_data(entity_id, object_id)
            else:
                logger.warning(f"Unsupported entity type: {entity_type}")
                return {}
                
        except Exception as e:
            logger.error(f"Error fetching data for {entity_type} {object_id}: {str(e)}")
            return {}
    
    def _get_authentication_state(self):
        """
        Get the current authentication state.
        
        Returns:
            dict: Authentication state information
        """
        # This would be implemented to check the current auth state
        # For simplicity, we'll simulate a connected state
        return {"status": "connected"}
    
    def _get_deals(self):
        """
        Get all deals from the external system.
        
        Returns:
            list: Array of deal objects with id and name
        """
        try:
            response = self._api_client.get_deals()
            
            return [
                {
                    "id": deal["id"],
                    "name": deal["name"]
                }
                for deal in response.get("deals", [])
            ]
        except Exception as e:
            logger.error(f"Error fetching deals: {str(e)}")
            return []
    
    def _get_deal_data(self, deal_id):
        """
        Get complete data for a specific deal.
        
        Args:
            deal_id (str): The ID of the deal
        
        Returns:
            dict: Complete deal data
        """
        try:
            deal_data = self._api_client.get_deal(deal_id)
            
            # Transform the API response to match the entity schema
            return {
                "id": deal_data["id"],
                "name": deal_data["name"],
                "amount": deal_data.get("amount"),
                "stage": deal_data.get("stage"),
                "close_date": deal_data.get("close_date"),
                "owner": {
                    "id": deal_data.get("owner", {}).get("id"),
                    "name": deal_data.get("owner", {}).get("name"),
                    "email": deal_data.get("owner", {}).get("email")
                },
                "contacts": [
                    {
                        "id": contact.get("id"),
                        "name": contact.get("name"),
                        "email": contact.get("email")
                    }
                    for contact in deal_data.get("contacts", [])
                ]
            }
        except Exception as e:
            logger.error(f"Error fetching deal data for {deal_id}: {str(e)}")
            return {}
    
    def _get_companies(self):
        """
        Get all companies from the external system.
        
        Returns:
            list: Array of company objects with id and name
        """
        try:
            response = self._api_client.get_companies()
            
            return [
                {
                    "id": company["id"],
                    "name": company["name"]
                }
                for company in response.get("companies", [])
            ]
        except Exception as e:
            logger.error(f"Error fetching companies: {str(e)}")
            return []
    
    def _get_company_data(self, company_id):
        """
        Get complete data for a specific company.
        
        Args:
            company_id (str): The ID of the company
        
        Returns:
            dict: Complete company data
        """
        try:
            company_data = self._api_client.get_company(company_id)
            
            # Transform the API response to match the entity schema
            return {
                "id": company_data["id"],
                "name": company_data["name"],
                "domain": company_data.get("domain"),
                "industry": company_data.get("industry"),
                "size": company_data.get("size"),
                "address": {
                    "street": company_data.get("address", {}).get("street"),
                    "city": company_data.get("address", {}).get("city"),
                    "state": company_data.get("address", {}).get("state"),
                    "postal_code": company_data.get("address", {}).get("postal_code"),
                    "country": company_data.get("address", {}).get("country")
                }
            }
        except Exception as e:
            logger.error(f"Error fetching company data for {company_id}: {str(e)}")
            return {}
    
    def _get_contacts(self):
        """
        Get all contacts from the external system.
        
        Returns:
            list: Array of contact objects with id and name
        """
        try:
            response = self._api_client.get_contacts()
            
            return [
                {
                    "id": contact["id"],
                    "name": f"{contact.get('first_name', '')} {contact.get('last_name', '')}".strip()
                }
                for contact in response.get("contacts", [])
            ]
        except Exception as e:
            logger.error(f"Error fetching contacts: {str(e)}")
            return []
    
    def _get_contact_data(self, contact_id):
        """
        Get complete data for a specific contact.
        
        Args:
            contact_id (str): The ID of the contact
        
        Returns:
            dict: Complete contact data
        """
        try:
            contact_data = self._api_client.get_contact(contact_id)
            
            # Transform the API response to match the entity schema
            return {
                "id": contact_data["id"],
                "first_name": contact_data.get("first_name"),
                "last_name": contact_data.get("last_name"),
                "email": contact_data.get("email"),
                "phone": contact_data.get("phone"),
                "job_title": contact_data.get("job_title"),
                "company": {
                    "id": contact_data.get("company", {}).get("id"),
                    "name": contact_data.get("company", {}).get("name")
                }
            }
        except Exception as e:
            logger.error(f"Error fetching contact data for {contact_id}: {str(e)}")
            return {}
    
    def _get_custom_objects(self, entity_id):
        """
        Get all instances of a custom object type.
        
        Args:
            entity_id (str): The ID of the custom object type
        
        Returns:
            list: Array of custom object instances with id and name
        """
        try:
            response = self._api_client.get_custom_objects(entity_id)
            
            return [
                {
                    "id": obj["id"],
                    "name": obj["name"]
                }
                for obj in response.get("objects", [])
            ]
        except Exception as e:
            logger.error(f"Error fetching custom objects for {entity_id}: {str(e)}")
            return []
    
    def _get_custom_object_data(self, entity_id, object_id):
        """
        Get complete data for a specific custom object instance.
        
        Args:
            entity_id (str): The ID of the custom object type
            object_id (str): The ID of the custom object instance
        
        Returns:
            dict: Complete custom object data
        """
        try:
            obj_data = self._api_client.get_custom_object(entity_id, object_id)
            
            # Transform the API response based on the object type
            return self._transform_custom_object(obj_data, entity_id)
            
        except Exception as e:
            logger.error(f"Error fetching custom object data for {entity_id}/{object_id}: {str(e)}")
            return {}
    
    def _transform_custom_object(self, obj_data, entity_id):
        """
        Transform custom object data to match the entity schema.
        
        Args:
            obj_data (dict): Raw custom object data from the API
            entity_id (str): The ID of the custom object type
        
        Returns:
            dict: Transformed custom object data
        """
        # This transformation would depend on the specific custom object type
        # For simplicity, we'll just return the raw data
        # In a real implementation, you would map fields appropriately
        return obj_data