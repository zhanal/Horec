from django.urls import path
from .views import PurchaseListView, PurchaseCreateView, PurchaseDetailView, PurchaseUpdateView, PurchaseDeleteView, add_to_purchase, add_single_item_to_purchase, remove_single_item_from_purchase, open_file
app_name = 'purchases'

urlpatterns = [
    path('', PurchaseListView, name='purchase-list'),
    path('<int:pk>/', PurchaseDetailView.as_view(), name='purchase-detail'),
    path('<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase-update'),
    path('<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('add-to-purchase/<int:pk>/', add_to_purchase, name='add-to-purchase'),
    path('create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('remove-single-item-from-purchase/<int:pk>/', remove_single_item_from_purchase, name='remove-single-item-from-purchase'),
    path('add_single_item_to_purchase/<int:pk>/', add_single_item_to_purchase, name='add-single-item-to-purchase'),
    path('<int:pk>/open_file/', open_file, name='open-file'),
    # path('<int:pk>/invoice/', order_invoice.as_view(), name='order-invoice'),
    # path('<int:pk>/invoice_pdf/', GenerateInvoicePdf.as_view(), name='order-invoice-pdf'),

]