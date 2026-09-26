from netbox.views import generic
from utilities.views import register_model_view
from netbox_uc import filtersets, forms, models, tables

__all__ = (
    'UserAccountListView',
    'UserAccountView',
    'UserAccountEditView',
    'UserAccountDeleteView',
    'UserAccountBulkImportView',
    'UserAccountBulkEditView',
    'UserAccountBulkDeleteView',
)


class UserAccountListView(generic.ObjectListView):
    queryset = models.UserAccount.objects.prefetch_related('platform', 'phone_number', 'site', 'tenant')
    table = tables.UserAccountTable
    filterset = filtersets.UserAccountFilterSet
    filterset_form = forms.UserAccountFilterForm


@register_model_view(models.UserAccount)
class UserAccountView(generic.ObjectView):
    queryset = models.UserAccount.objects.all()


@register_model_view(models.UserAccount, 'edit')
class UserAccountEditView(generic.ObjectEditView):
    queryset = models.UserAccount.objects.all()
    form = forms.UserAccountForm


@register_model_view(models.UserAccount, 'delete')
class UserAccountDeleteView(generic.ObjectDeleteView):
    queryset = models.UserAccount.objects.all()


class UserAccountBulkImportView(generic.BulkImportView):
    queryset = models.UserAccount.objects.all()
    model_form = forms.UserAccountImportForm


class UserAccountBulkEditView(generic.BulkEditView):
    queryset = models.UserAccount.objects.all()
    filterset = filtersets.UserAccountFilterSet
    table = tables.UserAccountTable
    form = forms.UserAccountBulkEditForm


class UserAccountBulkDeleteView(generic.BulkDeleteView):
    queryset = models.UserAccount.objects.all()
    filterset = filtersets.UserAccountFilterSet
    table = tables.UserAccountTable
