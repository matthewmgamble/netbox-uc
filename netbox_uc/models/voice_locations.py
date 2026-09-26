from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import SyncStatusChoices

__all__ = (
    'VoiceLocation',
)


class VoiceLocation(NetBoxModel):
    name = models.CharField(
        max_length=200,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_voice_locations',
        blank=True,
        null=True,
    )
    location = models.ForeignKey(
        to='dcim.Location',
        on_delete=models.SET_NULL,
        related_name='uc_voice_locations',
        blank=True,
        null=True,
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='voice_locations',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_voice_locations',
        blank=True,
        null=True,
    )
    emergency_address = models.ForeignKey(
        to='netbox_uc.EmergencyAddress',
        on_delete=models.SET_NULL,
        related_name='voice_locations',
        blank=True,
        null=True,
    )
    emergency_callback_number = models.ForeignKey(
        to='netbox_uc.PhoneNumber',
        on_delete=models.SET_NULL,
        related_name='callback_voice_locations',
        blank=True,
        null=True,
    )
    shared_calling_resource_account = models.ForeignKey(
        to='netbox_uc.ResourceAccount',
        on_delete=models.SET_NULL,
        related_name='shared_calling_voice_locations',
        blank=True,
        null=True,
        verbose_name='Shared Calling Resource Account',
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
        verbose_name_plural = 'voice locations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:voicelocation', args=[self.pk])
