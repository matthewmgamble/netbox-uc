from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import ResourceAccountTypeChoices, ServiceStatusChoices, SyncStatusChoices

__all__ = (
    'ResourceAccount',
)


class ResourceAccount(NetBoxModel):
    display_name = models.CharField(
        max_length=200,
    )
    user_principal_name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='User Principal Name',
    )
    object_id = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Object ID',
        help_text='Microsoft Entra object ID',
    )
    resource_account_type = models.CharField(
        max_length=50,
        choices=ResourceAccountTypeChoices,
        verbose_name='Type',
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='resource_accounts',
        blank=True,
        null=True,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_resource_accounts',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_resource_accounts',
        blank=True,
        null=True,
    )
    phone_number = models.ForeignKey(
        to='netbox_uc.PhoneNumber',
        on_delete=models.SET_NULL,
        related_name='resource_accounts',
        blank=True,
        null=True,
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
        ordering = ('display_name',)
        verbose_name_plural = 'resource accounts'

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:resourceaccount', args=[self.pk])
