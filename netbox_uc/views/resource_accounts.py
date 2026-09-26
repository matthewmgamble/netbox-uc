from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'ResourceAccountListView',
    'ResourceAccountView',
    'ResourceAccountEditView',
    'ResourceAccountDeleteView',
    'ResourceAccountBulkImportView',
    'ResourceAccountBulkEditView',
    'ResourceAccountBulkDeleteView',
)


class ResourceAccountListView(generic.ObjectListView):
    queryset = models.ResourceAccount.objects.prefetch_related('platform', 'site', 'phone_number', 'tenant')
    table = tables.ResourceAccountTable
    filterset = filtersets.ResourceAccountFilterSet
    filterset_form = forms.ResourceAccountFilterForm


@register_model_view(models.ResourceAccount)
class ResourceAccountView(generic.ObjectView):
    queryset = models.ResourceAccount.objects.all()


@register_model_view(models.ResourceAccount, 'edit')
class ResourceAccountEditView(generic.ObjectEditView):
    queryset = models.ResourceAccount.objects.all()
    form = forms.ResourceAccountForm


@register_model_view(models.ResourceAccount, 'delete')
class ResourceAccountDeleteView(generic.ObjectDeleteView):
    queryset = models.ResourceAccount.objects.all()


class ResourceAccountBulkImportView(generic.BulkImportView):
    queryset = models.ResourceAccount.objects.all()
    model_form = forms.ResourceAccountImportForm


class ResourceAccountBulkEditView(generic.BulkEditView):
    queryset = models.ResourceAccount.objects.all()
    filterset = filtersets.ResourceAccountFilterSet
    table = tables.ResourceAccountTable
    form = forms.ResourceAccountBulkEditForm


class ResourceAccountBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ResourceAccount.objects.all()
    filterset = filtersets.ResourceAccountFilterSet
    table = tables.ResourceAccountTable
