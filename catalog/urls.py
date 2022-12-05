from django.urls import path
from .views import (
    CatalogListView, CatalogDetailView, CatalogCreateView, CatalogUpdateView, CatalogDeleteView,
    CategoryListView, CategoryDetailView, 
    CatalogDetailOrderView, SummaryView, add_to_cart, remove_from_cart, remove_single_item_from_cart,
    CatalogDetailPurchaseView, CatalogDetailUpdateView, CatalogLineListView
)

app_name = 'catalog' #our app name 

urlpatterns = [
    path('', CatalogListView, name='catalog-list'),
    path('line/', CatalogLineListView, name='catalog-line-list'),

    path('<int:pk>/', CatalogDetailView.as_view(), name='catalog-detail'),
    path('<int:pk>/update/', CatalogUpdateView.as_view(), name='catalog-update'),
    path('<int:pk>/detail_update/', CatalogDetailUpdateView.as_view(), name='catalog-detail-update'),
    path('<int:pk>/delete/', CatalogDeleteView.as_view(), name='catalog-delete'),
    path('create/', CatalogCreateView.as_view(), name='catalog-create'),
    
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('summary/', SummaryView.as_view(), name='summary'),
    path('remove-item-from-cart/<int:pk>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),

    path('<int:pk>/orders/', CatalogDetailOrderView.as_view(), name='catalog-orders'),
    path('<int:pk>/purchases/', CatalogDetailPurchaseView.as_view(), name='catalog-purchases'),

]