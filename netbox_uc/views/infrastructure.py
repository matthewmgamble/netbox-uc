from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'SIPTrunkListView',
    'SIPTrunkView',
    'SIPTrunkEditView',
    'SIPTrunkDeleteView',
    'SIPTrunkBulkImportView',
    'SIPTrunkBulkEditView',
    'SIPTrunkBulkDeleteView',
    'SIPTrunkEndpointListView',
    'SIPTrunkEndpointView',
    'SIPTrunkEndpointEditView',
    'SIPTrunkEndpointDeleteView',
    'SIPTrunkEndpointBulkImportView',
    'SIPTrunkEndpointBulkEditView',
    'SIPTrunkEndpointBulkDeleteView',
    'SessionBorderControllerListView',
    'SessionBorderControllerView',
    'SessionBorderControllerEditView',
    'SessionBorderControllerDeleteView',
    'SessionBorderControllerBulkImportView',
    'SessionBorderControllerBulkEditView',
    'SessionBorderControllerBulkDeleteView',
)


#
# SIP Trunk
#

class SIPTrunkListView(generic.ObjectListView):
    queryset = models.SIPTrunk.objects.prefetch_related('carrier', 'platform', 'site', 'tenant')
    table = tables.SIPTrunkTable
    filterset = filtersets.SIPTrunkFilterSet
    filterset_form = forms.SIPTrunkFilterForm


@register_model_view(models.SIPTrunk)
class SIPTrunkView(generic.ObjectView):
    queryset = models.SIPTrunk.objects.all()


@register_model_view(models.SIPTrunk, 'edit')
class SIPTrunkEditView(generic.ObjectEditView):
    queryset = models.SIPTrunk.objects.all()
    form = forms.SIPTrunkForm


@register_model_view(models.SIPTrunk, 'delete')
class SIPTrunkDeleteView(generic.ObjectDeleteView):
    queryset = models.SIPTrunk.objects.all()


class SIPTrunkBulkImportView(generic.BulkImportView):
    queryset = models.SIPTrunk.objects.all()
    model_form = forms.SIPTrunkImportForm


class SIPTrunkBulkEditView(generic.BulkEditView):
    queryset = models.SIPTrunk.objects.all()
    filterset = filtersets.SIPTrunkFilterSet
    table = tables.SIPTrunkTable
    form = forms.SIPTrunkBulkEditForm


class SIPTrunkBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SIPTrunk.objects.all()
    filterset = filtersets.SIPTrunkFilterSet
    table = tables.SIPTrunkTable


#
# SIP Trunk Endpoint
#

class SIPTrunkEndpointListView(generic.ObjectListView):
    queryset = models.SIPTrunkEndpoint.objects.prefetch_related('sip_trunk')
    table = tables.SIPTrunkEndpointTable
    filterset = filtersets.SIPTrunkEndpointFilterSet
    filterset_form = forms.SIPTrunkEndpointFilterForm


@register_model_view(models.SIPTrunkEndpoint)
class SIPTrunkEndpointView(generic.ObjectView):
    queryset = models.SIPTrunkEndpoint.objects.all()


@register_model_view(models.SIPTrunkEndpoint, 'edit')
class SIPTrunkEndpointEditView(generic.ObjectEditView):
    queryset = models.SIPTrunkEndpoint.objects.all()
    form = forms.SIPTrunkEndpointForm


@register_model_view(models.SIPTrunkEndpoint, 'delete')
class SIPTrunkEndpointDeleteView(generic.ObjectDeleteView):
    queryset = models.SIPTrunkEndpoint.objects.all()


class SIPTrunkEndpointBulkImportView(generic.BulkImportView):
    queryset = models.SIPTrunkEndpoint.objects.all()
    model_form = forms.SIPTrunkEndpointImportForm


class SIPTrunkEndpointBulkEditView(generic.BulkEditView):
    queryset = models.SIPTrunkEndpoint.objects.all()
    filterset = filtersets.SIPTrunkEndpointFilterSet
    table = tables.SIPTrunkEndpointTable
    form = forms.SIPTrunkEndpointBulkEditForm


class SIPTrunkEndpointBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SIPTrunkEndpoint.objects.all()
    filterset = filtersets.SIPTrunkEndpointFilterSet
    table = tables.SIPTrunkEndpointTable


#
# Session Border Controller
#

class SessionBorderControllerListView(generic.ObjectListView):
    queryset = models.SessionBorderController.objects.prefetch_related('device', 'platform', 'tenant')
    table = tables.SessionBorderControllerTable
    filterset = filtersets.SessionBorderControllerFilterSet
    filterset_form = forms.SessionBorderControllerFilterForm


@register_model_view(models.SessionBorderController)
class SessionBorderControllerView(generic.ObjectView):
    queryset = models.SessionBorderController.objects.all()


@register_model_view(models.SessionBorderController, 'edit')
class SessionBorderControllerEditView(generic.ObjectEditView):
    queryset = models.SessionBorderController.objects.all()
    form = forms.SessionBorderControllerForm


@register_model_view(models.SessionBorderController, 'delete')
class SessionBorderControllerDeleteView(generic.ObjectDeleteView):
    queryset = models.SessionBorderController.objects.all()


class SessionBorderControllerBulkImportView(generic.BulkImportView):
    queryset = models.SessionBorderController.objects.all()
    model_form = forms.SessionBorderControllerImportForm


class SessionBorderControllerBulkEditView(generic.BulkEditView):
    queryset = models.SessionBorderController.objects.all()
    filterset = filtersets.SessionBorderControllerFilterSet
    table = tables.SessionBorderControllerTable
    form = forms.SessionBorderControllerBulkEditForm


class SessionBorderControllerBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SessionBorderController.objects.all()
    filterset = filtersets.SessionBorderControllerFilterSet
    table = tables.SessionBorderControllerTable
