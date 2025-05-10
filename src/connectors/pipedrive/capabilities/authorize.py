import logging
import json
import os
from typing import Dict, Any, Optional
from ..integration_connector.capabilities.authorize import AuthorizeCapability

logger = logging.getLogger(__name__)

class PipedriveAuthorizeCapability(AuthorizeCapability):
    """
    Pipedrive authorize capability that extends the base authorize capability.
    Currently uses all base functionality without modifications.
    """
    pass 