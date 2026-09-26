import re

from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import NumberTypeChoices, PhoneNumberStatusChoices

__all__ = (
    'PhoneNumber',
)

E164_REGEX = re.compile(r'^\+[1-9]\d{1,14}$')

ASSIGNMENT_MODELS = (
    'netbox_uc.resourceaccount',
    'netbox_uc.voiceendpoint',
    'netbox_uc.useraccount',
    'netbox_uc.autoattendant',
    'netbox_uc.callqueue',
)


class PhoneNumber(NetBoxModel):
    number = models.CharField(
        max_length=32,
        unique=True,
        help_text='Phone number in E.164 format (e.g., +19055551234)',
    )
    extension = models.CharField(
        max_length=16,
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=PhoneNumberStatusChoices,
        default=PhoneNumberStatusChoices.STATUS_AVAILABLE,
    )
    number_type = models.CharField(
        max_length=50,
        choices=NumberTypeChoices,
        default=NumberTypeChoices.TYPE_DID,
        verbose_name='Type',
    )
    carrier = models.ForeignKey(
        to='netbox_uc.Carrier',
        on_delete=models.PROTECT,
        related_name='phone_numbers',
        blank=True,
        null=True,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_phone_numbers',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_phone_numbers',
        blank=True,
        null=True,
    )
    platform = models.ForeignKey(
        to='netbox_uc.UCPlatform',
        on_delete=models.PROTECT,
        related_name='phone_numbers',
        blank=True,
        null=True,
    )
    sip_trunk = models.ForeignKey(
        to='netbox_uc.SIPTrunk',
        on_delete=models.SET_NULL,
        related_name='phone_numbers',
        blank=True,
        null=True,
    )
    assigned_object_type = models.ForeignKey(
        to='contenttypes.ContentType',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
    )
    assigned_object_id = models.PositiveBigIntegerField(
        blank=True,
        null=True,
    )
    assigned_object = GenericForeignKey(
        ct_field='assigned_object_type',
        fk_field='assigned_object_id',
    )
    description = models.CharField(
        max_length=200,
        blank=True,
    )
    comments = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ('number',)
        verbose_name_plural = 'phone numbers'

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:phonenumber', args=[self.pk])

    def clean(self):
        super().clean()

        # Validate E.164 format
        if self.number and not E164_REGEX.match(self.number):
            raise ValidationError({
                'number': 'Phone number must be in E.164 format (e.g., +19055551234).',
            })

        # Validate assigned_object type
        if self.assigned_object_type:
            model_label = f'{self.assigned_object_type.app_label}.{self.assigned_object_type.model}'
            if model_label not in ASSIGNMENT_MODELS:
                raise ValidationError({
                    'assigned_object_type': f'Phone numbers cannot be assigned to {model_label}.',
                })
