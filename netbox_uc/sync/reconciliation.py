"""Reconciliation engine for detecting drift between source systems and NetBox UC."""

import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

from django.db.models import Q

from netbox_uc.choices import SyncStatusChoices
from netbox_uc.models import (
    AutoAttendant, CallQueue, ResourceAccount, VoiceEndpoint, VoiceLocation,
)

logger = logging.getLogger('netbox_uc.sync.reconciliation')

# Models that support sync metadata
SYNCABLE_MODELS = [
    ResourceAccount,
    AutoAttendant,
    CallQueue,
    VoiceEndpoint,
    VoiceLocation,
]


@dataclass
class ReconciliationSummary:
    """Summary of reconciliation status across all syncable models."""
    healthy: int = 0
    missing: int = 0
    stale: int = 0
    archived: int = 0
    conflict: int = 0
    unsynced: int = 0
    per_model: dict = field(default_factory=dict)

    @property
    def total_synced(self):
        return self.healthy + self.missing + self.stale + self.archived + self.conflict

    def to_dict(self):
        return {
            'healthy': self.healthy,
            'missing': self.missing,
            'stale': self.stale,
            'archived': self.archived,
            'conflict': self.conflict,
            'unsynced': self.unsynced,
            'total_synced': self.total_synced,
            'per_model': self.per_model,
        }


def get_reconciliation_summary() -> ReconciliationSummary:
    """Build a summary of sync health across all syncable models."""
    summary = ReconciliationSummary()

    for model in SYNCABLE_MODELS:
        model_name = model._meta.label
        qs = model.objects.all()

        counts = {
            'healthy': qs.filter(sync_status=SyncStatusChoices.STATUS_HEALTHY).count(),
            'missing': qs.filter(sync_status=SyncStatusChoices.STATUS_MISSING).count(),
            'stale': qs.filter(sync_status=SyncStatusChoices.STATUS_STALE).count(),
            'archived': qs.filter(sync_status=SyncStatusChoices.STATUS_ARCHIVED).count(),
            'conflict': qs.filter(sync_status=SyncStatusChoices.STATUS_CONFLICT).count(),
            'unsynced': qs.filter(Q(sync_status='') | Q(sync_status__isnull=True)).count(),
        }

        summary.healthy += counts['healthy']
        summary.missing += counts['missing']
        summary.stale += counts['stale']
        summary.archived += counts['archived']
        summary.conflict += counts['conflict']
        summary.unsynced += counts['unsynced']
        summary.per_model[model_name] = counts

    return summary


def promote_missing_to_stale(stale_after_syncs: int = 3):
    """Promote objects that have been 'missing' for too many sync cycles to 'stale'.

    This is a simplified version that uses last_synced timestamp.
    Objects missing for longer than `stale_after_syncs` days are promoted.
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=stale_after_syncs)
    total_promoted = 0

    for model in SYNCABLE_MODELS:
        count = model.objects.filter(
            sync_status=SyncStatusChoices.STATUS_MISSING,
            last_synced__lt=cutoff,
        ).update(sync_status=SyncStatusChoices.STATUS_STALE)

        if count:
            logger.info(
                "Promoted %d %s objects from missing to stale",
                count, model._meta.label,
            )
            total_promoted += count

    return total_promoted


def promote_stale_to_archived(archive_after_days: int = 30):
    """Archive objects that have been stale beyond the retention period."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=archive_after_days)
    total_archived = 0

    for model in SYNCABLE_MODELS:
        count = model.objects.filter(
            sync_status=SyncStatusChoices.STATUS_STALE,
            last_synced__lt=cutoff,
        ).update(sync_status=SyncStatusChoices.STATUS_ARCHIVED)

        if count:
            logger.info(
                "Archived %d %s objects",
                count, model._meta.label,
            )
            total_archived += count

    return total_archived
