from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'NumberRangeListView',
    'NumberRangeView',
    'NumberRangeEditView',
    'NumberRangeDeleteView',
    'NumberRangeBulkImportView',
    'NumberRangeBulkEditView',
    'NumberRangeBulkDeleteView',
)


class NumberRangeListView(generic.ObjectListView):
    queryset = models.NumberRange.objects.prefetch_related('carrier', 'site', 'tenant')
    table = tables.NumberRangeTable
    filterset = filtersets.NumberRangeFilterSet
    filterset_form = forms.NumberRangeFilterForm


@register_model_view(models.NumberRange)
class NumberRangeView(generic.ObjectView):
    queryset = models.NumberRange.objects.all()


@register_model_view(models.NumberRange, 'edit')
class NumberRangeEditView(generic.ObjectEditView):
    queryset = models.NumberRange.objects.all()
    form = forms.NumberRangeForm


@register_model_view(models.NumberRange, 'delete')
class NumberRangeDeleteView(generic.ObjectDeleteView):
    queryset = models.NumberRange.objects.all()


class NumberRangeBulkImportView(generic.BulkImportView):
    queryset = models.NumberRange.objects.all()
    model_form = forms.NumberRangeImportForm


class NumberRangeBulkEditView(generic.BulkEditView):
    queryset = models.NumberRange.objects.all()
    filterset = filtersets.NumberRangeFilterSet
    table = tables.NumberRangeTable
    form = forms.NumberRangeBulkEditForm


class NumberRangeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.NumberRange.objects.all()
    filterset = filtersets.NumberRangeFilterSet
    table = tables.NumberRangeTable
