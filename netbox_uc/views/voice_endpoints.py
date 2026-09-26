from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'VoiceEndpointListView',
    'VoiceEndpointView',
    'VoiceEndpointEditView',
    'VoiceEndpointDeleteView',
    'VoiceEndpointBulkImportView',
    'VoiceEndpointBulkEditView',
    'VoiceEndpointBulkDeleteView',
)


class VoiceEndpointListView(generic.ObjectListView):
    queryset = models.VoiceEndpoint.objects.prefetch_related(
        'platform', 'site', 'device', 'phone_number', 'tenant', 'manufacturer',
    )
    table = tables.VoiceEndpointTable
    filterset = filtersets.VoiceEndpointFilterSet
    filterset_form = forms.VoiceEndpointFilterForm


@register_model_view(models.VoiceEndpoint)
class VoiceEndpointView(generic.ObjectView):
    queryset = models.VoiceEndpoint.objects.all()


@register_model_view(models.VoiceEndpoint, 'edit')
class VoiceEndpointEditView(generic.ObjectEditView):
    queryset = models.VoiceEndpoint.objects.all()
    form = forms.VoiceEndpointForm


@register_model_view(models.VoiceEndpoint, 'delete')
class VoiceEndpointDeleteView(generic.ObjectDeleteView):
    queryset = models.VoiceEndpoint.objects.all()


class VoiceEndpointBulkImportView(generic.BulkImportView):
    queryset = models.VoiceEndpoint.objects.all()
    model_form = forms.VoiceEndpointImportForm


class VoiceEndpointBulkEditView(generic.BulkEditView):
    queryset = models.VoiceEndpoint.objects.all()
    filterset = filtersets.VoiceEndpointFilterSet
    table = tables.VoiceEndpointTable
    form = forms.VoiceEndpointBulkEditForm


class VoiceEndpointBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VoiceEndpoint.objects.all()
    filterset = filtersets.VoiceEndpointFilterSet
    table = tables.VoiceEndpointTable
