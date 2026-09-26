from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import ServiceStatusChoices, SyncStatusChoices

__all__ = (
    'CallQueue',
)


class CallQueue(NetBoxModel):
    name = models.CharField(
        max_length=200,
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='call_queues',
        blank=True,
        null=True,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_call_queues',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_call_queues',
        blank=True,
        null=True,
    )
    resource_account = models.ForeignKey(
        to='netbox_uc.ResourceAccount',
        on_delete=models.SET_NULL,
        related_name='call_queues',
        blank=True,
        null=True,
    )
    phone_numbers = models.ManyToManyField(
        to='netbox_uc.PhoneNumber',
        related_name='call_queues',
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=ServiceStatusChoices,
        default=ServiceStatusChoices.STATUS_ACTIVE,
    )
    external_id = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='External ID',
    )
    sync_status = models.CharField(
        max_length=50,
        choices=SyncStatusChoices,
        blank=True,
    )
    last_synced = models.DateTimeField(
        blank=True,
        null=True,
    )
    description = models.CharField(
        max_length=200,
        blank=True,
    )
    comments = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'call queues'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:callqueue', args=[self.pk])
