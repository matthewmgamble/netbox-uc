import logging
from typing import Any

import httpx

from .auth import MicrosoftAuthClient

logger = logging.getLogger('netbox_uc.sync.microsoft')

GRAPH_BASE_URL = 'https://graph.microsoft.com'
GRAPH_V1 = f'{GRAPH_BASE_URL}/v1.0'
GRAPH_BETA = f'{GRAPH_BASE_URL}/beta'


class GraphClient:
    """Microsoft Graph API client for Teams Calling data."""

    def __init__(self, auth: MicrosoftAuthClient):
        self.auth = auth
        self._client = None

    @property
    def client(self) -> httpx.Client:
        if self._client is None:
            self._client = httpx.Client(
                headers={
                    'Authorization': f'Bearer {self.auth.token}',
                    'Content-Type': 'application/json',
                },
                timeout=30.0,
            )
        return self._client

    def _get_paginated(self, url: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages of a paginated Graph API response."""
        results = []
        while url:
            response = self.client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            results.extend(data.get('value', []))
            url = data.get('@odata.nextLink')
            params = None  # nextLink includes params
        return results

    def get_resource_accounts(self) -> list[dict]:
        """Fetch Teams resource accounts (users with Phone System Virtual User license)."""
        # Resource accounts are users with the PHONESYSTEM_VIRTUALUSER license
        url = f'{GRAPH_V1}/users'
        params = {
            '$filter': "assignedLicenses/any(l:l/skuId eq '440eaaa8-b3e0-484b-a8be-62870b9ba70a')",
            '$select': 'id,displayName,userPrincipalName,assignedLicenses',
            '$top': '999',
        }
        logger.info("Fetching resource accounts from Microsoft Graph")
        return self._get_paginated(url, params)

    def get_auto_attendants(self) -> list[dict]:
        """Fetch Teams auto attendants."""
        url = f'{GRAPH_BETA}/communications/callQueues'
        # Note: Auto attendants use a different beta endpoint
        url = f'{GRAPH_BETA}/communications/autoAttendants'
        params = {'$top': '999'}
        logger.info("Fetching auto attendants from Microsoft Graph")
        try:
            return self._get_paginated(url, params)
        except httpx.HTTPStatusError as e:
            logger.warning("Failed to fetch auto attendants: %s", e)
            return []

    def get_call_queues(self) -> list[dict]:
        """Fetch Teams call queues."""
        url = f'{GRAPH_BETA}/communications/callQueues'
        params = {'$top': '999'}
        logger.info("Fetching call queues from Microsoft Graph")
        try:
            return self._get_paginated(url, params)
        except httpx.HTTPStatusError as e:
            logger.warning("Failed to fetch call queues: %s", e)
            return []

    def get_phone_numbers(self) -> list[dict]:
        """Fetch Teams phone numbers."""
        url = f'{GRAPH_BETA}/communications/phoneNumbers'
        params = {'$top': '999'}
        logger.info("Fetching phone numbers from Microsoft Graph")
        try:
            return self._get_paginated(url, params)
        except httpx.HTTPStatusError as e:
            logger.warning("Failed to fetch phone numbers: %s", e)
            return []

    def close(self):
        """Close the HTTP client."""
        if self._client:
            self._client.close()
            self._client = None
