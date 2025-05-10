import os
import logging
from ..utils.helpers import load_yaml_file, get_localization_file_path, deep_merge

logger = logging.getLogger(__name__)

class LocalizationCapability:
    """
    Implements the Localization capability which provides translations
    for properties related to all objects within the integration.
    """
    
    def __init__(self, config, api_client):
        """
        Initialize the Localization capability.
        
        Args:
            config (dict): The integration configuration
            api_client (ApiClient): The API client instance
        """
        self.config = config
        self._api_client = api_client
        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.strings = {}
        self.default_lang = 'en'
    
    def configure(self, strings):
        """
        Configure the localization strings.
        
        Args:
            strings (dict): Dictionary of language codes to string mappings
        """
        self.strings = strings
    
    def get_string(self, key, lang=None):
        """
        Get a localized string for the given key and language.
        
        Args:
            key (str): The string key to look up
            lang (str, optional): Language code. Defaults to default_lang.
            
        Returns:
            str: The localized string
            
        Raises:
            KeyError: If the string is not found in any language
        """
        if not lang:
            lang = self.default_lang
            
        # Try to get the string in the requested language
        if lang in self.strings and key in self.strings[lang]:
            return self.strings[lang][key]
            
        # Fall back to default language if not found
        if lang != self.default_lang and self.default_lang in self.strings and key in self.strings[self.default_lang]:
            return self.strings[self.default_lang][key]
            
        # Raise KeyError if not found in any language
        raise KeyError(f"String '{key}' not found in language '{lang}' or default language")
    
    def get_localization(self, lang='en'):
        """
        Return localization data for the specified language.
        
        Args:
            lang (str): Language code (e.g., 'en', 'it'). Default is 'en'.
        
        Returns:
            dict: Localization data for the specified language
        """
        # Get the default localization data
        default_path = get_localization_file_path(self.base_dir)
        default_localization = load_yaml_file(default_path)
        
        # If the requested language is English, return the default
        if not lang or lang.lower() == 'en':
            return default_localization
        
        # Try to load language-specific localization
        try:
            lang_path = get_localization_file_path(self.base_dir, lang)
            if os.path.exists(lang_path):
                lang_localization = load_yaml_file(lang_path)
                
                # Merge with default localization (language-specific takes precedence)
                return deep_merge(default_localization, lang_localization)
            else:
                logger.warning(f"Localization file for language '{lang}' not found. Using default.")
                return default_localization
                
        except Exception as e:
            logger.error(f"Error loading localization for language '{lang}': {str(e)}")
            return default_localization