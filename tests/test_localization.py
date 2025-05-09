import unittest
import os
import sys
from unittest.mock import MagicMock, patch
import pytest

# Add the parent directory to the Python path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chimera.integration_connector.capabilities.localization import LocalizationCapability
from chimera.integration_connector.api.client import ApiClient

class TestLocalizationCapability(unittest.TestCase):
    """Test suite for the LocalizationCapability class."""
    
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock config
        self.config = {}
        
        # Create a mock API client
        self.api_client = MagicMock(spec=ApiClient)
        
        # Create patches for external dependencies
        self.load_yaml_patcher = patch('chimera.integration_connector.capabilities.localization.load_yaml_file')
        self.get_path_patcher = patch('chimera.integration_connector.capabilities.localization.get_localization_file_path')
        self.os_path_exists_patcher = patch('os.path.exists')
        
        # Start the patches
        self.mock_load_yaml = self.load_yaml_patcher.start()
        self.mock_get_path = self.get_path_patcher.start()
        self.mock_os_path_exists = self.os_path_exists_patcher.start()
        
        # Configure the mocks
        self.default_localization = {
            'info': {
                'description': 'Connect PandaDoc with your CRM system',
                'overview': 'Seamlessly create documents from your CRM data'
            },
            'entities': {
                'deal': 'Deal',
                'company': 'Company',
                'contact': 'Contact'
            },
            'actions': {
                'update': 'Update',
                'attach_document': 'Attach Document',
                'add_history': 'Add History'
            }
        }
        
        self.italian_localization = {
            'info': {
                'description': 'Collega PandaDoc con il tuo sistema CRM',
                'overview': 'Crea documenti dal tuo CRM in modo semplice e veloce'
            },
            'entities': {
                'deal': 'Trattativa',
                'company': 'Azienda',
                'contact': 'Contatto'
            },
            'actions': {
                'update': 'Aggiorna',
                'attach_document': 'Allega Documento',
                'add_history': 'Aggiungi Cronologia'
            }
        }
        
        # Set up the mock to return different values based on the language
        self.mock_load_yaml.side_effect = lambda path: (
            self.default_localization if 'localization.yaml' in path
            else self.italian_localization if 'localization_IT.yaml' in path
            else {}
        )
        
        # Set up the mock to return the appropriate paths
        self.mock_get_path.side_effect = lambda base_dir, lang=None: (
            os.path.join(base_dir, 'localization.yaml') if not lang or lang.lower() == 'en'
            else os.path.join(base_dir, f'localization_{lang.upper()}.yaml')
        )
        
        # Set up the mock to return True for existing files
        self.mock_os_path_exists.side_effect = lambda path: True
        
        # Create an instance of the capability
        self.localization_capability = LocalizationCapability(self.config, self.api_client)
    
    def tearDown(self):
        """Tear down test fixtures after each test method is run."""
        self.load_yaml_patcher.stop()
        self.get_path_patcher.stop()
        self.os_path_exists_patcher.stop()
    
    def test_get_localization_default(self):
        """Test that get_localization returns the default localization when no language is specified."""
        localization = self.localization_capability.get_localization()
        
        self.assertEqual(localization, self.default_localization)
        self.mock_load_yaml.assert_called_once()
        self.mock_get_path.assert_called_once_with(self.localization_capability.base_dir)
    
    def test_get_localization_english(self):
        """Test that get_localization returns the default localization when English is specified."""
        localization = self.localization_capability.get_localization('en')
        
        self.assertEqual(localization, self.default_localization)
        self.mock_load_yaml.assert_called_once()
        self.mock_get_path.assert_called_once_with(self.localization_capability.base_dir)
    
    def test_get_localization_italian(self):
        """Test that get_localization returns the Italian localization when Italian is specified."""
        localization = self.localization_capability.get_localization('it')
        
        self.assertEqual(localization, self.italian_localization)
        self.assertEqual(self.mock_load_yaml.call_count, 2)  # Default + Italian
        self.mock_get_path.assert_any_call(self.localization_capability.base_dir)
        self.mock_get_path.assert_any_call(self.localization_capability.base_dir, 'it')
    
    def test_get_localization_missing_language_file(self):
        """Test that get_localization returns the default localization when the language file is missing."""
        # Set up the mock to return False for non-default files
        self.mock_os_path_exists.side_effect = lambda path: 'localization.yaml' in path
        
        localization = self.localization_capability.get_localization('fr')
        
        self.assertEqual(localization, self.default_localization)
        self.mock_load_yaml.assert_called_once()
        self.mock_get_path.assert_any_call(self.localization_capability.base_dir)
        self.mock_get_path.assert_any_call(self.localization_capability.base_dir, 'fr')
    
    def test_get_localization_error_loading(self):
        """Test that get_localization handles errors when loading localization files."""
        # Set up the mock to raise an exception for non-default files
        original_side_effect = self.mock_load_yaml.side_effect
        
        def new_side_effect(path):
            if 'localization_DE.yaml' in path:
                raise Exception("Error loading file")
            return original_side_effect(path)
        
        self.mock_load_yaml.side_effect = new_side_effect
        
        # Try to get German localization
        localization = self.localization_capability.get_localization('de')
        
        # Should return default localization on error
        self.assertEqual(localization, self.default_localization)

@pytest.fixture
def mock_config():
    return {
        'localization': {
            'en': {
                'integration_name': 'Test Integration',
                'description': 'Test Description'
            }
        }
    }

@pytest.fixture
def mock_api_client():
    return MagicMock(spec=ApiClient)

def test_localization_capability_initialization(mock_config, mock_api_client):
    """Test localization capability initialization."""
    capability = LocalizationCapability(mock_config, mock_api_client)
    assert capability.strings == {}
    assert capability.default_lang == 'en'

def test_configure_localization(mock_config, mock_api_client):
    """Test configuring localization."""
    capability = LocalizationCapability(mock_config, mock_api_client)
    strings = {
        'en': {
            'integration_name': 'Test Integration',
            'description': 'Test Description'
        }
    }
    capability.configure(strings)
    assert capability.strings == strings

def test_get_string(mock_config, mock_api_client):
    """Test getting localized string."""
    capability = LocalizationCapability(mock_config, mock_api_client)
    strings = {
        'en': {
            'integration_name': 'Test Integration',
            'description': 'Test Description'
        },
        'es': {
            'integration_name': 'Integración de Prueba',
            'description': 'Descripción de Prueba'
        }
    }
    capability.configure(strings)
    
    # Test default language
    assert capability.get_string('integration_name') == 'Test Integration'
    
    # Test specific language
    assert capability.get_string('integration_name', 'es') == 'Integración de Prueba'

def test_get_string_fallback(mock_config, mock_api_client):
    """Test string fallback to default language."""
    capability = LocalizationCapability(mock_config, mock_api_client)
    strings = {
        'en': {
            'integration_name': 'Test Integration'
        }
    }
    capability.configure(strings)
    
    # Should fallback to English when string doesn't exist in requested language
    assert capability.get_string('integration_name', 'es') == 'Test Integration'

def test_get_string_not_found(mock_config, mock_api_client):
    """Test getting non-existent string."""
    capability = LocalizationCapability(mock_config, mock_api_client)
    strings = {
        'en': {
            'integration_name': 'Test Integration'
        }
    }
    capability.configure(strings)
    
    with pytest.raises(KeyError):
        capability.get_string('non_existent')

if __name__ == '__main__':
    unittest.main()