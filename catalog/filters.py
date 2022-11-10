import django_filters
from .models import * 

class CatalogFilter(django_filters.FilterSet):
    class Meta: 
        model = Catalog
        fields = [
            'brand',
            'model',
            'category',
            'subcategory',
            'sell_price',
        ]

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = [
            'organisation',
            'project',
            'client',
            'status',
            'manager',
            # 'deadline',
        ]

class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase
        fields = [
            'organisation',
            'project',
            'seller',
            'status',
            'manager',
            # 'deadline',
        ]