class ConnectorError(Exception):
    """Base exception for all connector errors."""
    pass

class AuthenticationError(ConnectorError):
    """Raised when authentication fails."""
    pass

class AuthorizationError(ConnectorError):
    """Raised when authorization fails."""
    pass

class EntityNotFoundError(ConnectorError):
    """Raised when an entity type is not found."""
    pass

class ObjectNotFoundError(ConnectorError):
    """Raised when an object is not found."""
    pass

class ActionNotFoundError(ConnectorError):
    """Raised when an action is not found."""
    pass

class ValidationError(ConnectorError):
    """Raised when data validation fails."""
    pass

class ConfigurationError(ConnectorError):
    """Raised when there's an issue with the connector configuration."""
    pass 