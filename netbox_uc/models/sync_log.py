from django.db import models
from django.urls import reverse

__all__ = (
    'SyncLog',
)


class SyncLog(models.Model):
    """Records the result of each synchronization run."""

    sync_source = models.CharField(
        max_length=100,
        help_text='Source adapter name (e.g., microsoft-teams-resource-accounts)',
    )
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=50,
        default='running',
        help_text='success, failed, partial, running',
    )
    created_count = models.IntegerField(default=0)
    updated_count = models.IntegerField(default=0)
    unchanged_count = models.IntegerField(default=0)
    missing_count = models.IntegerField(default=0)
    error_count = models.IntegerField(default=0)
    errors = models.JSONField(
        default=list,
        blank=True,
    )
    dry_run = models.BooleanField(default=False)

    class Meta:
        ordering = ('-started_at',)
        verbose_name = 'sync log'
        verbose_name_plural = 'sync logs'

    def __str__(self):
        return f'{self.sync_source} - {self.started_at}'

    @property
    def duration(self):
        if self.completed_at and self.started_at:
            return (self.completed_at - self.started_at).total_seconds()
        return None

    @property
    def total_processed(self):
        return self.created_count + self.updated_count + self.unchanged_count + self.missing_count
