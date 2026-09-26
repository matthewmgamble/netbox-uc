from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from netbox_uc.choices import NumberRangeStatusChoices, PhoneNumberStatusChoices

__all__ = (
    'NumberRange',
)


class NumberRange(NetBoxModel):
    name = models.CharField(
        max_length=100,
    )
    start_number = models.CharField(
        max_length=32,
        help_text='First number in the range (E.164 format)',
    )
    end_number = models.CharField(
        max_length=32,
        help_text='Last number in the range (E.164 format)',
    )
    carrier = models.ForeignKey(
        to='netbox_uc.Carrier',
        on_delete=models.PROTECT,
        related_name='number_ranges',
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=50,
        choices=NumberRangeStatusChoices,
        default=NumberRangeStatusChoices.STATUS_ACTIVE,
    )
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.SET_NULL,
        related_name='uc_number_ranges',
        blank=True,
        null=True,
    )
    tenant = models.ForeignKey(
        to='tenancy.Tenant',
        on_delete=models.PROTECT,
        related_name='uc_number_ranges',
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
        verbose_name_plural = 'number ranges'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_uc:numberrange', args=[self.pk])

    def clean(self):
        super().clean()
        if self.start_number and self.end_number:
            try:
                start = int(self.start_number.lstrip('+'))
                end = int(self.end_number.lstrip('+'))
                if end < start:
                    raise ValidationError({
                        'end_number': 'End number must be greater than or equal to start number.',
                    })
            except ValueError:
                pass

    @property
    def total_numbers(self):
        try:
            start = int(self.start_number.lstrip('+'))
            end = int(self.end_number.lstrip('+'))
            return end - start + 1
        except (ValueError, TypeError):
            return 0

    @property
    def phone_numbers_in_range(self):
        from netbox_uc.models import PhoneNumber
        if not self.start_number or not self.end_number:
            return PhoneNumber.objects.none()
        return PhoneNumber.objects.filter(
            number__gte=self.start_number,
            number__lte=self.end_number,
        )

    @property
    def assigned_count(self):
        return self.phone_numbers_in_range.filter(
            status=PhoneNumberStatusChoices.STATUS_ASSIGNED,
        ).count()

    @property
    def available_count(self):
        return self.phone_numbers_in_range.filter(
            status=PhoneNumberStatusChoices.STATUS_AVAILABLE,
        ).count()

    @property
    def reserved_count(self):
        return self.phone_numbers_in_range.filter(
            status=PhoneNumberStatusChoices.STATUS_RESERVED,
        ).count()
