from django.urls import  path
from .views import ( OrderListView, OrderCreateView, OrderDetailView, OrderUpdateView, OrderDeleteView,
                        add_to_order, remove_single_item_from_order, add_single_item_to_order, open_file, order_invoice, GenerateInvoicePdf
                    ) 

app_name = 'orders'

urlpatterns = [
    path('', OrderListView, name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update', OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete', OrderDeleteView.as_view(), name='order-delete'),
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/add-to-order/', add_to_order, name='add-to-order'),
    path('remove-single-item-from-order/<int:pk>/', remove_single_item_from_order, name='remove-single-item-from-order'),
    path('add_single_item_to_order/<int:pk>/', add_single_item_to_order, name='add-single-item-to-order'),
    path('<int:pk>/open_file/', open_file, name='open-file'),
    path('<int:pk>/invoice/', order_invoice.as_view(), name='order-invoice'),
    path('<int:pk>/invoice_pdf/', GenerateInvoicePdf.as_view(), name='order-invoice-pdf'),
]