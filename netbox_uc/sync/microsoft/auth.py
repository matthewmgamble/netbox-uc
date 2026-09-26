import logging

import msal

logger = logging.getLogger('netbox_uc.sync.microsoft')

GRAPH_SCOPES = ['https://graph.microsoft.com/.default']


class MicrosoftAuthClient:
    """OAuth2 client credentials authentication for Microsoft Graph API."""

    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self._app = None
        self._token = None

    @property
    def app(self):
        if self._app is None:
            self._app = msal.ConfidentialClientApplication(
                client_id=self.client_id,
                client_credential=self.client_secret,
                authority=f'https://login.microsoftonline.com/{self.tenant_id}',
            )
        return self._app

    def get_token(self) -> str:
        """Acquire an access token using client credentials flow."""
        result = self.app.acquire_token_for_client(scopes=GRAPH_SCOPES)

        if 'access_token' in result:
            self._token = result['access_token']
            logger.debug("Successfully acquired Microsoft Graph access token")
            return self._token

        error = result.get('error', 'unknown')
        error_desc = result.get('error_description', 'No description')
        raise RuntimeError(
            f"Failed to acquire Microsoft Graph token: {error} - {error_desc}"
        )

    @property
    def token(self) -> str:
        if self._token is None:
            return self.get_token()
        return self._token
