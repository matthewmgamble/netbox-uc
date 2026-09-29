import logging
from dataclasses import dataclass, field
from typing import Any

from django.db.models import QuerySet

logger = logging.getLogger('netbox_uc.sync')


@dataclass
class SyncDiff:
    """Result of comparing source data to existing NetBox data."""
    new: list[dict] = field(default_factory=list)
    changed: list[tuple[Any, dict]] = field(default_factory=list)
    unchanged: list[Any] = field(default_factory=list)
    missing: list[Any] = field(default_factory=list)


@dataclass
class SyncResult:
    """Result of applying a sync diff."""
    created: int = 0
    updated: int = 0
    unchanged: int = 0
    missing: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def success(self):
        return len(self.errors) == 0

    @property
    def total_processed(self):
        return self.created + self.updated + self.unchanged + self.missing


class SourceAdapter:
    """Base class for all synchronization source adapters.

    Subclasses must implement authenticate(), discover(), normalize(),
    and get_existing(). The compare() and apply() methods provide
    default implementations that can be overridden.
    """

    name: str = 'unknown'

    def authenticate(self):
        """Establish authentication with the source system."""
        raise NotImplementedError

    def discover(self) -> list[dict]:
        """Discover objects from the source system.

        Returns raw data from the source API.
        """
        raise NotImplementedError

    def normalize(self, raw_data: list[dict]) -> list[dict]:
        """Normalize raw source data into a standard internal format.

        Each dict should contain:
        - 'external_id': unique identifier in the source system
        - All fields needed to create/update the NetBox model
        """
        raise NotImplementedError

    def get_existing(self) -> QuerySet:
        """Return the existing NetBox objects for this adapter's model."""
        raise NotImplementedError

    def get_external_id(self, obj) -> str:
        """Extract the external ID from a NetBox model instance."""
        return getattr(obj, 'external_id', '')

    def compare(self, normalized: list[dict], existing: QuerySet) -> SyncDiff:
        """Compare normalized source data against existing NetBox objects.

        Returns a SyncDiff describing what needs to change.
        """
        diff = SyncDiff()

        existing_by_id = {}
        for obj in existing:
            ext_id = self.get_external_id(obj)
            if ext_id:
                existing_by_id[ext_id] = obj

        source_ids = set()
        for item in normalized:
            ext_id = item.get('external_id', '')
            source_ids.add(ext_id)

            if ext_id in existing_by_id:
                obj = existing_by_id[ext_id]
                if self._has_changes(obj, item):
                    diff.changed.append((obj, item))
                else:
                    diff.unchanged.append(obj)
            else:
                diff.new.append(item)

        for ext_id, obj in existing_by_id.items():
            if ext_id not in source_ids:
                diff.missing.append(obj)

        return diff

    def _has_changes(self, obj, data: dict) -> bool:
        """Check if an existing object differs from the normalized data."""
        for key, value in data.items():
            if key == 'external_id':
                continue
            current = getattr(obj, key, None)
            if hasattr(current, 'pk'):
                # FK comparison
                if current.pk != value:
                    return True
            elif current != value:
                return True
        return False

    def create_object(self, data: dict):
        """Create a new NetBox object from normalized data."""
        raise NotImplementedError

    def update_object(self, obj, data: dict):
        """Update an existing NetBox object with normalized data."""
        raise NotImplementedError

    def mark_missing(self, obj):
        """Mark an object as missing from the source."""
        from netbox_uc.choices import SyncStatusChoices
        if hasattr(obj, 'sync_status'):
            obj.sync_status = SyncStatusChoices.STATUS_MISSING
            obj.save(update_fields=['sync_status'])

    def apply(self, diff: SyncDiff, dry_run: bool = False) -> SyncResult:
        """Apply a sync diff to NetBox.

        If dry_run is True, no changes are made.
        """
        result = SyncResult()

        for item in diff.new:
            if dry_run:
                result.created += 1
                continue
            try:
                self.create_object(item)
                result.created += 1
            except Exception:
                ext_id = item.get('external_id', '<unknown>')
                result.errors.append(f"Failed to create object {ext_id}")
                logger.error("Failed to create object: %s", ext_id, exc_info=logger.isEnabledFor(logging.DEBUG))

        for obj, item in diff.changed:
            if dry_run:
                result.updated += 1
                continue
            try:
                self.update_object(obj, item)
                result.updated += 1
            except Exception:
                result.errors.append(f"Failed to update object {obj}")
                logger.error("Failed to update object: %s", obj, exc_info=logger.isEnabledFor(logging.DEBUG))

        result.unchanged = len(diff.unchanged)

        for obj in diff.missing:
            if dry_run:
                result.missing += 1
                continue
            try:
                self.mark_missing(obj)
                result.missing += 1
            except Exception:
                result.errors.append(f"Failed to mark missing {obj}")
                logger.error("Failed to mark missing: %s", obj, exc_info=logger.isEnabledFor(logging.DEBUG))

        return result

    def sync(self, dry_run: bool = False) -> SyncResult:
        """Execute a full sync cycle: authenticate, discover, normalize, compare, apply."""
        logger.info("Starting sync for adapter: %s", self.name)

        self.authenticate()
        raw_data = self.discover()
        logger.info("Discovered %d objects from %s", len(raw_data), self.name)

        normalized = self.normalize(raw_data)
        existing = self.get_existing()
        existing_count = existing.count()

        # Safety check: refuse to mark all records missing when the source
        # returned nothing.  This prevents a Graph API outage or transient
        # error from wiping the entire dataset.
        if not normalized and existing_count > 0:
            logger.error(
                "Source returned 0 objects for %s but %d existing records found. "
                "Aborting sync to prevent data loss.",
                self.name, existing_count,
            )
            result = SyncResult()
            result.errors.append(
                f"Source returned 0 objects but {existing_count} existing records "
                f"found — aborting to prevent data loss."
            )
            return result

        diff = self.compare(normalized, existing)

        logger.info(
            "Sync diff for %s: %d new, %d changed, %d unchanged, %d missing",
            self.name, len(diff.new), len(diff.changed),
            len(diff.unchanged), len(diff.missing),
        )

        result = self.apply(diff, dry_run=dry_run)

        logger.info(
            "Sync result for %s: %d created, %d updated, %d unchanged, %d missing, %d errors",
            self.name, result.created, result.updated, result.unchanged,
            result.missing, len(result.errors),
        )

        return result
