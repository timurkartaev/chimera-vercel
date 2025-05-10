import logging

from ..integration_connector.api.client import ApiClient
# or, if the ApiClient is in a different package structure
# from integration_connector.api.client import ApiClient

logger = logging.getLogger(__name__)

class PipedriveApiClient(ApiClient):
    """
    Pipedrive API client that extends the base API client.
    Currently uses all base functionality without modifications.
    """
    pass

