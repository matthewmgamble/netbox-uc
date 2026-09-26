from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import SyncStatusChoices

__all__ = (
    'EmergencyAddress',
)


class EmergencyAddress(NetBoxModel):
    name = models.CharField(
        max_length=200,
    )
    street = models.CharField(
        max_length=200,
    )
    city = models.CharField(
        max_length=100,
    )
    province_state = models.CharField(
        max_length=100,
        verbose_name='Province/State',
    )
    postal_code = models.CharField(
        max_length=20,
    )
    country = models.CharField(
        max_length=100,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_emergency_addresses',
        blank=True,
        null=True,
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text='GPS latitude in decimal degrees',
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text='GPS longitude in decimal degrees',
    )
    validated = models.BooleanField(
        default=False,
        help_text='Whether this address has been validated for emergency calling',
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
        verbose_name_plural = 'emergency addresses'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:emergencyaddress', args=[self.pk])
