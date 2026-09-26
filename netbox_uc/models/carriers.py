from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

__all__ = (
    'Carrier',
)


class Carrier(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )
    account_number = models.CharField(
        max_length=100,
        blank=True,
    )
    support_contact = models.CharField(
        max_length=200,
        blank=True,
    )
    portal_url = models.URLField(
        blank=True,
        verbose_name='Portal URL',
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_carriers',
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
        verbose_name_plural = 'carriers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:carrier', args=[self.pk])
