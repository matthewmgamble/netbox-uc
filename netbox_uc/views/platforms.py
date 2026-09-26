from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'UCPlatformListView',
    'UCPlatformView',
    'UCPlatformEditView',
    'UCPlatformDeleteView',
    'UCPlatformBulkImportView',
    'UCPlatformBulkEditView',
    'UCPlatformBulkDeleteView',
)


class UCPlatformListView(generic.ObjectListView):
    queryset = models.UCPlatform.objects.all()
    table = tables.UCPlatformTable
    filterset = filtersets.UCPlatformFilterSet
    filterset_form = forms.UCPlatformFilterForm


@register_model_view(models.UCPlatform)
class UCPlatformView(generic.ObjectView):
    queryset = models.UCPlatform.objects.all()


@register_model_view(models.UCPlatform, 'edit')
class UCPlatformEditView(generic.ObjectEditView):
    queryset = models.UCPlatform.objects.all()
    form = forms.UCPlatformForm


@register_model_view(models.UCPlatform, 'delete')
class UCPlatformDeleteView(generic.ObjectDeleteView):
    queryset = models.UCPlatform.objects.all()


class UCPlatformBulkImportView(generic.BulkImportView):
    queryset = models.UCPlatform.objects.all()
    model_form = forms.UCPlatformImportForm


class UCPlatformBulkEditView(generic.BulkEditView):
    queryset = models.UCPlatform.objects.all()
    filterset = filtersets.UCPlatformFilterSet
    table = tables.UCPlatformTable
    form = forms.UCPlatformBulkEditForm


class UCPlatformBulkDeleteView(generic.BulkDeleteView):
    queryset = models.UCPlatform.objects.all()
    filterset = filtersets.UCPlatformFilterSet
    table = tables.UCPlatformTable
