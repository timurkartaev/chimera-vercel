import time
import logging
import functools
import os
import yaml
from functools import wraps
from typing import Type, Tuple, Callable, Any

logger = logging.getLogger(__name__)

def retry_with_backoff(
    max_retries: int = 3,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    backoff_factor: float = 1.5,
    initial_delay: float = 1.0
) -> Callable:
    """
    Decorator for retrying a function with exponential backoff.
    
    Args:
        max_retries: Maximum number of retry attempts
        exceptions: Tuple of exceptions to catch and retry
        backoff_factor: Multiplier for the delay between retries
        initial_delay: Initial delay in seconds
        
    Returns:
        Decorated function that will retry on specified exceptions
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_retries:
                        logger.error(f"Max retries ({max_retries}) exceeded. Last error: {str(e)}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying in {delay:.2f}s...")
                    time.sleep(delay)
                    delay *= backoff_factor
            
            # This should never be reached due to the raise in the loop
            raise last_exception
        
        return wrapper
    return decorator

def load_yaml_file(file_path):
    """
    Load YAML file and return its content.
    
    Args:
        file_path (str): Path to the YAML file
    
    Returns:
        dict: Parsed YAML content
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        yaml.YAMLError: If the file contains invalid YAML
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r') as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML file {file_path}: {str(e)}")
            raise

def get_localization_file_path(base_dir, lang=None):
    """
    Get the path to the localization file for a specific language.
    
    Args:
        base_dir (str): Base directory containing localization files
        lang (str, optional): Language code (e.g., 'en', 'it'). 
                            Default is None (uses default localization.yaml).
    
    Returns:
        str: Path to the localization file
    """
    if lang and lang.lower() != 'en':
        file_name = f"localization_{lang.upper()}.yaml"
    else:
        file_name = "localization.yaml"
    
    return os.path.join(base_dir, file_name)

def deep_merge(dict1, dict2):
    """
    Deep merge two dictionaries.
    
    If a key exists in both dictionaries, the value from dict2 will overwrite
    the value from dict1. If the value is a dictionary in both, they will be
    merged recursively.
    
    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary (takes precedence)
    
    Returns:
        dict: Merged dictionary
    """
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    
    return result

def transform_schema_to_flat(schema, parent_key=''):
    """
    Transform a nested JSON Schema to a flat dictionary for easy mapping.
    
    Args:
        schema (dict): JSON Schema object
        parent_key (str, optional): Parent key for nested properties
    
    Returns:
        dict: Flat dictionary with dot notation keys
    """
    flat_schema = {}
    
    if not schema or not isinstance(schema, dict):
        return flat_schema
    
    if 'properties' in schema and isinstance(schema['properties'], dict):
        for key, value in schema['properties'].items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            
            # Add this property
            flat_schema[new_key] = {
                'type': value.get('type'),
                'title': value.get('title', key),
                'format': value.get('format', None),
                'readonly': value.get('readonly', False)
            }
            
            # Handle nested objects
            if value.get('type') == 'object' and 'properties' in value:
                nested = transform_schema_to_flat(value, new_key)
                flat_schema.update(nested)
            
            # Handle arrays with object items
            if value.get('type') == 'array' and 'items' in value:
                items = value['items']
                if isinstance(items, dict) and items.get('type') == 'object':
                    array_prefix = f"{new_key}[]"
                    nested = transform_schema_to_flat({'properties': items.get('properties', {})}, array_prefix)
                    flat_schema.update(nested)
    
    return flat_schema

def validate_required_fields(data: dict, required_fields: list) -> None:
    """
    Validate that all required fields are present in the data.
    
    Args:
        data: Dictionary to validate
        required_fields: List of required field names
        
    Raises:
        ValueError: If any required field is missing
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

def format_error_message(error: Exception) -> str:
    """
    Format an error message in a consistent way.
    
    Args:
        error: The exception to format
        
    Returns:
        Formatted error message
    """
    return f"{error.__class__.__name__}: {str(error)}"