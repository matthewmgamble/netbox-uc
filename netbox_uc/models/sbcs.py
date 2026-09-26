from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import SBCRoleChoices, ServiceStatusChoices

__all__ = (
    'SessionBorderController',
)


class SessionBorderController(NetBoxModel):
    name = models.CharField(
        max_length=200,
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.SET_NULL,
        related_name='uc_sbcs',
        blank=True,
        null=True,
        help_text='Associated NetBox DCIM device',
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='sbcs',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_sbcs',
        blank=True,
        null=True,
    )
    role = models.CharField(
        max_length=50,
        choices=SBCRoleChoices,
    )
    status = models.CharField(
        max_length=50,
        choices=ServiceStatusChoices,
        default=ServiceStatusChoices.STATUS_ACTIVE,
    )
    sip_trunks = models.ManyToManyField(
        to='netbox_uc.SIPTrunk',
        related_name='sbcs',
        blank=True,
    )
    external_id = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='External ID',
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
        verbose_name = 'session border controller'
        verbose_name_plural = 'session border controllers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:sessionbordercontroller', args=[self.pk])
