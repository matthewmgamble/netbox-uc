from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'AutoAttendantListView',
    'AutoAttendantView',
    'AutoAttendantEditView',
    'AutoAttendantDeleteView',
    'AutoAttendantBulkImportView',
    'AutoAttendantBulkEditView',
    'AutoAttendantBulkDeleteView',
    'CallQueueListView',
    'CallQueueView',
    'CallQueueEditView',
    'CallQueueDeleteView',
    'CallQueueBulkImportView',
    'CallQueueBulkEditView',
    'CallQueueBulkDeleteView',
)


#
# Auto Attendant
#

class AutoAttendantListView(generic.ObjectListView):
    queryset = models.AutoAttendant.objects.prefetch_related('platform', 'site', 'resource_account', 'tenant')
    table = tables.AutoAttendantTable
    filterset = filtersets.AutoAttendantFilterSet
    filterset_form = forms.AutoAttendantFilterForm


@register_model_view(models.AutoAttendant)
class AutoAttendantView(generic.ObjectView):
    queryset = models.AutoAttendant.objects.all()


@register_model_view(models.AutoAttendant, 'edit')
class AutoAttendantEditView(generic.ObjectEditView):
    queryset = models.AutoAttendant.objects.all()
    form = forms.AutoAttendantForm


@register_model_view(models.AutoAttendant, 'delete')
class AutoAttendantDeleteView(generic.ObjectDeleteView):
    queryset = models.AutoAttendant.objects.all()


class AutoAttendantBulkImportView(generic.BulkImportView):
    queryset = models.AutoAttendant.objects.all()
    model_form = forms.AutoAttendantImportForm


class AutoAttendantBulkEditView(generic.BulkEditView):
    queryset = models.AutoAttendant.objects.all()
    filterset = filtersets.AutoAttendantFilterSet
    table = tables.AutoAttendantTable
    form = forms.AutoAttendantBulkEditForm


class AutoAttendantBulkDeleteView(generic.BulkDeleteView):
    queryset = models.AutoAttendant.objects.all()
    filterset = filtersets.AutoAttendantFilterSet
    table = tables.AutoAttendantTable


#
# Call Queue
#

class CallQueueListView(generic.ObjectListView):
    queryset = models.CallQueue.objects.prefetch_related('platform', 'site', 'resource_account', 'tenant')
    table = tables.CallQueueTable
    filterset = filtersets.CallQueueFilterSet
    filterset_form = forms.CallQueueFilterForm


@register_model_view(models.CallQueue)
class CallQueueView(generic.ObjectView):
    queryset = models.CallQueue.objects.all()


@register_model_view(models.CallQueue, 'edit')
class CallQueueEditView(generic.ObjectEditView):
    queryset = models.CallQueue.objects.all()
    form = forms.CallQueueForm


@register_model_view(models.CallQueue, 'delete')
class CallQueueDeleteView(generic.ObjectDeleteView):
    queryset = models.CallQueue.objects.all()


class CallQueueBulkImportView(generic.BulkImportView):
    queryset = models.CallQueue.objects.all()
    model_form = forms.CallQueueImportForm


class CallQueueBulkEditView(generic.BulkEditView):
    queryset = models.CallQueue.objects.all()
    filterset = filtersets.CallQueueFilterSet
    table = tables.CallQueueTable
    form = forms.CallQueueBulkEditForm


class CallQueueBulkDeleteView(generic.BulkDeleteView):
    queryset = models.CallQueue.objects.all()
    filterset = filtersets.CallQueueFilterSet
    table = tables.CallQueueTable
