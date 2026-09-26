from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'PhoneNumberListView',
    'PhoneNumberView',
    'PhoneNumberEditView',
    'PhoneNumberDeleteView',
    'PhoneNumberBulkImportView',
    'PhoneNumberBulkEditView',
    'PhoneNumberBulkDeleteView',
)


class PhoneNumberListView(generic.ObjectListView):
    queryset = models.PhoneNumber.objects.prefetch_related('carrier', 'site', 'platform', 'tenant')
    table = tables.PhoneNumberTable
    filterset = filtersets.PhoneNumberFilterSet
    filterset_form = forms.PhoneNumberFilterForm


@register_model_view(models.PhoneNumber)
class PhoneNumberView(generic.ObjectView):
    queryset = models.PhoneNumber.objects.all()


@register_model_view(models.PhoneNumber, 'edit')
class PhoneNumberEditView(generic.ObjectEditView):
    queryset = models.PhoneNumber.objects.all()
    form = forms.PhoneNumberForm


@register_model_view(models.PhoneNumber, 'delete')
class PhoneNumberDeleteView(generic.ObjectDeleteView):
    queryset = models.PhoneNumber.objects.all()


class PhoneNumberBulkImportView(generic.BulkImportView):
    queryset = models.PhoneNumber.objects.all()
    model_form = forms.PhoneNumberImportForm


class PhoneNumberBulkEditView(generic.BulkEditView):
    queryset = models.PhoneNumber.objects.all()
    filterset = filtersets.PhoneNumberFilterSet
    table = tables.PhoneNumberTable
    form = forms.PhoneNumberBulkEditForm


class PhoneNumberBulkDeleteView(generic.BulkDeleteView):
    queryset = models.PhoneNumber.objects.all()
    filterset = filtersets.PhoneNumberFilterSet
    table = tables.PhoneNumberTable
