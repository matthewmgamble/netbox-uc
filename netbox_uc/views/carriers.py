from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'CarrierListView',
    'CarrierView',
    'CarrierEditView',
    'CarrierDeleteView',
    'CarrierBulkImportView',
    'CarrierBulkEditView',
    'CarrierBulkDeleteView',
)


class CarrierListView(generic.ObjectListView):
    queryset = models.Carrier.objects.all()
    table = tables.CarrierTable
    filterset = filtersets.CarrierFilterSet
    filterset_form = forms.CarrierFilterForm


@register_model_view(models.Carrier)
class CarrierView(generic.ObjectView):
    queryset = models.Carrier.objects.all()


@register_model_view(models.Carrier, 'edit')
class CarrierEditView(generic.ObjectEditView):
    queryset = models.Carrier.objects.all()
    form = forms.CarrierForm


@register_model_view(models.Carrier, 'delete')
class CarrierDeleteView(generic.ObjectDeleteView):
    queryset = models.Carrier.objects.all()


class CarrierBulkImportView(generic.BulkImportView):
    queryset = models.Carrier.objects.all()
    model_form = forms.CarrierImportForm


class CarrierBulkEditView(generic.BulkEditView):
    queryset = models.Carrier.objects.all()
    filterset = filtersets.CarrierFilterSet
    table = tables.CarrierTable
    form = forms.CarrierBulkEditForm


class CarrierBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Carrier.objects.all()
    filterset = filtersets.CarrierFilterSet
    table = tables.CarrierTable
