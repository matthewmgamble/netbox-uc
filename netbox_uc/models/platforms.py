from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import UCPlatformStatusChoices

__all__ = (
    'UCPlatform',
)


class UCPlatform(NetBoxModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )
    platform_type = models.CharField(
        max_length=50,
        blank=True,
        help_text='Type of UC platform (e.g., Cloud PBX, On-Premises PBX)',
    )
    version = models.CharField(
        max_length=50,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=UCPlatformStatusChoices,
        default=UCPlatformStatusChoices.STATUS_ACTIVE,
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
        verbose_name = 'UC platform'
        verbose_name_plural = 'UC platforms'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:ucplatform', args=[self.pk])
