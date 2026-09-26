from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

__all__ = (
    'SIPTrunkEndpoint',
)


class SIPTrunkEndpoint(NetBoxModel):
    """A carrier-side signaling endpoint (FQDN or IP) for a SIP trunk, with priority for failover ordering."""

    sip_trunk = models.ForeignKey(
        to='netbox_uc.SIPTrunk',
        on_delete=models.CASCADE,
        related_name='endpoints',
    )
    fqdn_or_ip = models.CharField(
        max_length=255,
        verbose_name='FQDN / IP',
        help_text='Carrier signaling endpoint (e.g., sbc1.carrier.com or 203.0.113.10)',
    )
    port = models.PositiveIntegerField(
        default=5060,
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
    )
    protocol = models.CharField(
        max_length=20,
        blank=True,
        help_text='e.g., SIP TLS, SIP TCP, SIP UDP',
    )
    priority = models.PositiveSmallIntegerField(
        default=10,
        help_text='Lower values are preferred for failover (primary = 10, secondary = 20, etc.)',
    )
    description = models.CharField(
        max_length=200,
        blank=True,
    )

    class Meta:
        ordering = ('sip_trunk', 'priority', 'fqdn_or_ip')
        verbose_name = 'SIP trunk endpoint'
        verbose_name_plural = 'SIP trunk endpoints'
        unique_together = (('sip_trunk', 'fqdn_or_ip', 'port'),)

    def __str__(self):
        return f'{self.fqdn_or_ip}:{self.port}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:siptrunkendpoint', args=[self.pk])
