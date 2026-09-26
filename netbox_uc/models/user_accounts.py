from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import UserAccountStatusChoices

__all__ = (
    'UserAccount',
)


class UserAccount(NetBoxModel):
    display_name = models.CharField(
        max_length=200,
    )
    user_principal_name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='User Principal Name',
    )
    external_id = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='External ID',
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='user_accounts',
        blank=True,
        null=True,
    )
    phone_number = models.ForeignKey(
        to='netbox_uc.PhoneNumber',
        on_delete=models.SET_NULL,
        related_name='user_accounts',
        blank=True,
        null=True,
    )
    extension = models.CharField(
        max_length=16,
        blank=True,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_user_accounts',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_user_accounts',
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=50,
        choices=UserAccountStatusChoices,
        default=UserAccountStatusChoices.STATUS_ACTIVE,
    )
    description = models.CharField(
        max_length=200,
        blank=True,
    )
    comments = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ('display_name',)
        verbose_name_plural = 'user accounts'

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:useraccount', args=[self.pk])
