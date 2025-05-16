class InfoCapability:
    """
    Implements the Info capability which provides metadata about the integration.
    """
    
    def __init__(self, config, api_client):
        """
        Initialize the Info capability.
        
        Args:
            config (dict): The integration configuration
            api_client (ApiClient): The API client instance
        """
        self.config = config
        self._api_client = api_client
        self.info = {}
    
    def configure(self, info):
        """
        Configure the integration info.
        
        Args:
            info (dict): The integration info configuration
            
        Raises:
            ValueError: If required fields are missing
        """
        # Validate required fields
        required_fields = ['name', 'logo']
        for field in required_fields:
            if field not in info:
                raise ValueError(f"Missing required field '{field}' in info configuration")
        
        self.info = info
    
    def get_info(self):
        """
        Return integration info metadata.
        
        Returns:
            dict: The integration info metadata
        """
        # If info is configured, return it
        if self.info:
            return self.info
            
        # Otherwise, extract from config
        info = self.config.get('info', {})
        
        # Validate required fields
        required_fields = ['name', 'logo']
        for field in required_fields:
            if field not in info:
                raise ValueError(f"Missing required field '{field}' in info configuration")
        
        # Return the info section
        return {
            'logo': info.get('logo'),
            'name': info.get('name'),
            'categories': info.get('categories', []),
            'website': info.get('website'),
            'support_email': info.get('support_email'),
            'version': info.get('version'),
            'developer': info.get('developer')
        }