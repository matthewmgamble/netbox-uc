import logging
from datetime import datetime, timezone

from django.db.models import QuerySet

from netbox_uc.choices import (
    ResourceAccountTypeChoices, ServiceStatusChoices, SyncStatusChoices,
)
from netbox_uc.models import AutoAttendant, CallQueue, PhoneNumber, ResourceAccount
from netbox_uc.sync.base import SourceAdapter, SyncResult
from .auth import MicrosoftAuthClient
from .client import GraphClient
from .normalizers import (
    normalize_auto_attendant,
    normalize_call_queue,
    normalize_phone_number,
    normalize_resource_account,
)

logger = logging.getLogger('netbox_uc.sync.microsoft')


class TeamsResourceAccountAdapter(SourceAdapter):
    """Sync adapter for Microsoft Teams Resource Accounts."""

    name = 'microsoft-teams-resource-accounts'

    def __init__(self, tenant_id: str, client_id: str, client_secret: str, platform=None):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.platform = platform
        self._auth = None
        self._client = None

    def authenticate(self):
        self._auth = MicrosoftAuthClient(
            self.tenant_id, self.client_id, self.client_secret,
        )
        self._client = GraphClient(self._auth)

    def discover(self) -> list[dict]:
        return self._client.get_resource_accounts()

    def normalize(self, raw_data: list[dict]) -> list[dict]:
        return [normalize_resource_account(item) for item in raw_data]

    def get_existing(self) -> QuerySet:
        qs = ResourceAccount.objects.filter(external_id__gt='')
        if self.platform:
            qs = qs.filter(platform=self.platform)
        return qs

    def create_object(self, data: dict):
        now = datetime.now(timezone.utc)
        ResourceAccount.objects.create(
            display_name=data['display_name'],
            user_principal_name=data['user_principal_name'],
            object_id=data.get('object_id', ''),
            resource_account_type=ResourceAccountTypeChoices.TYPE_AUTO_ATTENDANT,
            platform=self.platform,
            status=ServiceStatusChoices.STATUS_ACTIVE,
            external_id=data['external_id'],
            sync_status=SyncStatusChoices.STATUS_HEALTHY,
            last_synced=now,
        )

    def update_object(self, obj, data: dict):
        now = datetime.now(timezone.utc)
        obj.display_name = data['display_name']
        obj.user_principal_name = data['user_principal_name']
        obj.object_id = data.get('object_id', obj.object_id)
        obj.sync_status = SyncStatusChoices.STATUS_HEALTHY
        obj.last_synced = now
        obj.save()


class TeamsAutoAttendantAdapter(SourceAdapter):
    """Sync adapter for Microsoft Teams Auto Attendants."""

    name = 'microsoft-teams-auto-attendants'

    def __init__(self, tenant_id: str, client_id: str, client_secret: str, platform=None):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.platform = platform
        self._auth = None
        self._client = None

    def authenticate(self):
        self._auth = MicrosoftAuthClient(
            self.tenant_id, self.client_id, self.client_secret,
        )
        self._client = GraphClient(self._auth)

    def discover(self) -> list[dict]:
        return self._client.get_auto_attendants()

    def normalize(self, raw_data: list[dict]) -> list[dict]:
        return [normalize_auto_attendant(item) for item in raw_data]

    def get_existing(self) -> QuerySet:
        qs = AutoAttendant.objects.filter(external_id__gt='')
        if self.platform:
            qs = qs.filter(platform=self.platform)
        return qs

    def create_object(self, data: dict):
        now = datetime.now(timezone.utc)
        AutoAttendant.objects.create(
            name=data['name'],
            platform=self.platform,
            status=ServiceStatusChoices.STATUS_ACTIVE,
            timezone=data.get('timezone', ''),
            language=data.get('language', ''),
            external_id=data['external_id'],
            sync_status=SyncStatusChoices.STATUS_HEALTHY,
            last_synced=now,
        )

    def update_object(self, obj, data: dict):
        now = datetime.now(timezone.utc)
        obj.name = data['name']
        obj.timezone = data.get('timezone', obj.timezone)
        obj.language = data.get('language', obj.language)
        obj.sync_status = SyncStatusChoices.STATUS_HEALTHY
        obj.last_synced = now
        obj.save()


class TeamsCallQueueAdapter(SourceAdapter):
    """Sync adapter for Microsoft Teams Call Queues."""

    name = 'microsoft-teams-call-queues'

    def __init__(self, tenant_id: str, client_id: str, client_secret: str, platform=None):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.platform = platform
        self._auth = None
        self._client = None

    def authenticate(self):
        self._auth = MicrosoftAuthClient(
            self.tenant_id, self.client_id, self.client_secret,
        )
        self._client = GraphClient(self._auth)

    def discover(self) -> list[dict]:
        return self._client.get_call_queues()

    def normalize(self, raw_data: list[dict]) -> list[dict]:
        return [normalize_call_queue(item) for item in raw_data]

    def get_existing(self) -> QuerySet:
        qs = CallQueue.objects.filter(external_id__gt='')
        if self.platform:
            qs = qs.filter(platform=self.platform)
        return qs

    def create_object(self, data: dict):
        now = datetime.now(timezone.utc)
        CallQueue.objects.create(
            name=data['name'],
            platform=self.platform,
            status=ServiceStatusChoices.STATUS_ACTIVE,
            external_id=data['external_id'],
            sync_status=SyncStatusChoices.STATUS_HEALTHY,
            last_synced=now,
        )

    def update_object(self, obj, data: dict):
        now = datetime.now(timezone.utc)
        obj.name = data['name']
        obj.sync_status = SyncStatusChoices.STATUS_HEALTHY
        obj.last_synced = now
        obj.save()


class TeamsPhoneNumberAdapter(SourceAdapter):
    """Sync adapter for Microsoft Teams Phone Numbers."""

    name = 'microsoft-teams-phone-numbers'

    def __init__(self, tenant_id: str, client_id: str, client_secret: str, platform=None):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.platform = platform
        self._auth = None
        self._client = None

    def authenticate(self):
        self._auth = MicrosoftAuthClient(
            self.tenant_id, self.client_id, self.client_secret,
        )
        self._client = GraphClient(self._auth)

    def discover(self) -> list[dict]:
        return self._client.get_phone_numbers()

    def normalize(self, raw_data: list[dict]) -> list[dict]:
        return [normalize_phone_number(item) for item in raw_data]

    def get_existing(self) -> QuerySet:
        qs = PhoneNumber.objects.all()
        if self.platform:
            qs = qs.filter(platform=self.platform)
        return qs

    def get_external_id(self, obj) -> str:
        # Phone numbers use the number itself as external ID if no external_id set
        return obj.number

    def create_object(self, data: dict):
        PhoneNumber.objects.create(
            number=data['number'],
            number_type=data.get('number_type', 'did'),
            status=data.get('status', 'available'),
            platform=self.platform,
        )

    def update_object(self, obj, data: dict):
        obj.status = data.get('status', obj.status)
        obj.number_type = data.get('number_type', obj.number_type)
        obj.save()
