from django import forms
from catalog.models import Purchase

class PurchaseModelForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = (
            'organisation',
            'project',
            'deadline',
            'pickup_date',
            'name',
            'seller',
            'status',
            'files',
            'received',
            'paid',
            'discount',
            'proforma',
        )
