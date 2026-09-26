from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import SyncStatusChoices, VoiceEndpointStatusChoices, VoiceEndpointTypeChoices

__all__ = (
    'VoiceEndpoint',
)


class VoiceEndpoint(NetBoxModel):
    name = models.CharField(
        max_length=200,
    )
    endpoint_type = models.CharField(
        max_length=50,
        choices=VoiceEndpointTypeChoices,
        verbose_name='Type',
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='voice_endpoints',
        blank=True,
        null=True,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_voice_endpoints',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_voice_endpoints',
        blank=True,
        null=True,
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.SET_NULL,
        related_name='uc_voice_endpoints',
        blank=True,
        null=True,
        help_text='Associated NetBox DCIM device',
    )
    interface = models.ForeignKey(
        to='dcim.Interface',
        on_delete=models.SET_NULL,
        related_name='uc_voice_endpoints',
        blank=True,
        null=True,
    )
    phone_number = models.ForeignKey(
        to='netbox_uc.PhoneNumber',
        on_delete=models.SET_NULL,
        related_name='voice_endpoints',
        blank=True,
        null=True,
    )
    user_account = models.ForeignKey(
        to='netbox_uc.UserAccount',
        on_delete=models.SET_NULL,
        related_name='voice_endpoints',
        blank=True,
        null=True,
    )
    resource_account = models.ForeignKey(
        to='netbox_uc.ResourceAccount',
        on_delete=models.SET_NULL,
        related_name='voice_endpoints',
        blank=True,
        null=True,
    )
    manufacturer = models.ForeignKey(
        to='dcim.Manufacturer',
        on_delete=models.PROTECT,
        related_name='uc_voice_endpoints',
        blank=True,
        null=True,
    )
    model = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Model',
    )
    serial_number = models.CharField(
        max_length=100,
        blank=True,
    )
    mac_address = models.CharField(
        max_length=18,
        blank=True,
        verbose_name='MAC Address',
    )
    firmware = models.CharField(
        max_length=100,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=VoiceEndpointStatusChoices,
        default=VoiceEndpointStatusChoices.STATUS_ACTIVE,
    )
    last_seen = models.DateTimeField(
        blank=True,
        null=True,
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
        verbose_name_plural = 'voice endpoints'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:voiceendpoint', args=[self.pk])
