from django import forms
from .models import Catalog, Brand, Client, Organisation, Manager

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class CatalogModelForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = [
            'name',
            'brand',
            'model',
            'category',
            'sell_price',
        ]

class DetailedCatalogModelForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = [
        'name',
        'brand',
        'model',
        'article',
        'category',
        'subcategory',
        'code',
        'external_code',
        'barcode',
        'zone',
        'description',
        'hs_code',
        'country',
        'customs_tax',
        'transport_coefficient',
        'margin_coefficient',
        'stock_qty',
        'purchase_price',
        'sell_price',
        'min_sell_price',
        'max_sell_price',
        'image',
        ]
        
        fields_order = [
        'name',
        'brand',
        'model',
        'article',
        'category',
        'subcategory',
        'code',
        'external_code',
        'barcode',
        'zone',
        'description',
        'hs_code',
        'country',
        'customs_tax',
        'transport_coefficient',
        'margin_coefficient',
        'stock_qty',
        'purchase_price',
        'sell_price',
        'min_sell_price',
        'max_sell_price',
        'image',
        ]

class CatalogForm(forms.Form):
    name = forms.CharField()
    brand = forms.CharField() 
    model = forms.CharField()
    category = forms.CharField()
    sell_price = forms.IntegerField()


class DetailedCatalogForm(forms.Form):
    name = forms.CharField()
    brand = forms.CharField() 
    model = forms.CharField()
    artilce = forms.CharField()
    category = forms.CharField()
    subcategory = forms.CharField()
    code = forms.CharField()
    external_code = forms.CharField()
    barcode = forms.CharField()
    zone = forms.CharField()
    description = forms.CharField()
    hs_code = forms.IntegerField()
    customs_tax = forms.FloatField()
    country = forms.CharField()
    transport_coefficient = forms.FloatField()
    margin_coefficient = forms.FloatField()
    stock_qty = forms.IntegerField(min_value=0)
    purchase_price = forms.IntegerField()
    sell_price = forms.IntegerField()
    
    image = forms.ImageField()
    

class CustomUserCreationForm(UserCreationForm):
       class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            'name',
            'country',
            'contact_person',
            'phone',
            'email',
            'bank',
            'bank_acc',
            'bik',
        ]

class BrandForm(forms.Form):
    name = forms.CharField()
    country = forms.CharField()
    contact_person = forms.CharField()
    phone = forms.IntegerField()
    email = forms.EmailField()
    bank = forms.CharField()
    bank_acc = forms.CharField()
    bik = forms.CharField()

class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'contact_person',
            'phone',
            'email',
            'bank',
            'bank',
            'bank_acc',
            'bik',
        ]

class ClientForm(forms.Form):
    name = forms.CharField()
    contact_person = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    bank = forms.CharField()
    bank = forms.CharField()
    bank_acc = forms.CharField()
    bik = forms.CharField()

class OrganisationModelForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = [
            'name',
            'contact_person',
            'phone',
            'email',
            'bank',
            'bank_acc',
            'bik',
        ]

class OrganisationForm(forms.Form):
    name = forms.CharField()
    contact_person = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    bank = forms.CharField()
    bank_acc = forms.CharField()
    bik = forms.CharField()
