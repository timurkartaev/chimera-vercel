import datetime
import uuid

import jwt
from django.conf import settings


class AuthenticateCapability:

    def __init__(self, config, api_client):
        self.config = config

    def _get_user_token(self):
        encoded_jwt = jwt.encode(
            {
                "id": "",
                "name": "Timur Kartaev",
                "iss": settings.IPAAS_WORKSPACE_KEY,
                "fields": {},
                "exp": datetime.datetime.now() + datetime.timedelta(minutes=5),
            },
            settings.IPAAS_WORKSPACE_SECRET,
            algorithm="HS256",
        )
        return encoded_jwt

    def get_authenticate_url(self):
        token = self._get_user_token()
        return (
            f"https://api.integration.app/connection-popup?"
            f"token={token}&requestId={uuid.uuid4()}&integrationKey={self.config.info.slug}"
        )

    def get_callback_url(self):
        pass