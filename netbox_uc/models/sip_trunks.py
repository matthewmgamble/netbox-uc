from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import SIPTrunkDirectionChoices, SIPTrunkStatusChoices

__all__ = (
    'SIPTrunk',
)


class SIPTrunk(NetBoxModel):
    name = models.CharField(
        max_length=200,
    )
    carrier = models.ForeignKey(
        to='netbox_uc.Carrier',
        on_delete=models.PROTECT,
        related_name='sip_trunks',
        blank=True,
        null=True,
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='sip_trunks',
        blank=True,
        null=True,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_sip_trunks',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_sip_trunks',
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=50,
        choices=SIPTrunkStatusChoices,
        default=SIPTrunkStatusChoices.STATUS_ACTIVE,
    )
    direction = models.CharField(
        max_length=50,
        choices=SIPTrunkDirectionChoices,
        default=SIPTrunkDirectionChoices.DIRECTION_BIDIRECTIONAL,
    )
    signaling_protocol = models.CharField(
        max_length=50,
        blank=True,
        help_text='e.g., SIP TLS, SIP TCP, SIP UDP',
    )
    media_protocol = models.CharField(
        max_length=50,
        blank=True,
        help_text='e.g., SRTP, RTP',
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
        verbose_name = 'SIP trunk'
        verbose_name_plural = 'SIP trunks'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:siptrunk', args=[self.pk])
