from django.contrib import admin
from .models import (
    User, UserProfile, Manager, Brand, Client, Organisation, Project,
    Catalog, Cart, Order, Purchase,
    Category, Subcategory, OrderItem, OrderedItem, PurchasedItem,
)

admin.site.register(User)
admin.site.register(UserProfile)

admin.site.register(Manager)
admin.site.register(Brand)
admin.site.register(Client)
admin.site.register(Organisation)
admin.site.register(Project)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Catalog)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderedItem)

admin.site.register(Cart)
admin.site.register(Purchase)
admin.site.register(PurchasedItem)
