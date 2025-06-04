from apps.connectors.base.connector import ConnectorConfig


class IpaasClient:
    def __init__(self, config: ConnectorConfig):
        self.config = config

    def start_auth_flow(self, user_id, redirect_uri):
        return {
            "auth_url": f"https://auth.ipaas.com/start?user={user_id}&redirect_uri={redirect_uri}"
        }

    def finalize_auth(self, code, state):
        return {"status": "connected", "access_token": "xyz-token"}
