from django import forms 
from catalog.models import Order, OrderedItem
from djmoney.forms.fields import MoneyField

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'organisation',
            'project',
            'deadline',
            'shipment_date',
            'name',
            'client',
            'status',
            'files',
            'received',
            'shipped',
            'discount',
            'files',
        )

    # items = forms.ModelMultipleChoiceField(
    #     queryset=OrderedItem.objects.all(),
    #     widget = forms.CheckboxSelectMultiple
    #     )
    
class OrderForm(forms.Form):
    organisation = forms.ChoiceField()
    project = forms.ChoiceField()
    deadline = forms.DateField()
    shipment_date = forms.DateField()
    name = forms.CharField()
    client = forms.ChoiceField()
    status = forms.ChoiceField()
    files = forms.FileField
    received = MoneyField()
    shipped = forms.IntegerField()
    discount = forms.FloatField()
    files = forms.FileField()

class OrderedItemModelForm(forms.ModelForm):
    model = OrderedItem
    fields = (
        'quantity',
        'discount'
    )

class OrderedItemForm(forms.Form):
    quantity = forms.IntegerField()
    discount = forms.FloatField()