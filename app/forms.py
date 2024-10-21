from django import forms
from django.forms import Textarea
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'customer_name',
            'email',
            'address',
            'comment',
            'calculation',
            'cost',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = Textarea(attrs={'rows': 3})
        self.fields['customer_name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your e-mail'
        self.fields['address'].widget.attrs['placeholder'] = 'Your address'
        self.fields['comment'].widget.attrs['placeholder'] = 'Comment'
        self.fields['calculation'].widget.attrs['hidden'] = 'true'
        self.fields['cost'].widget.attrs['hidden'] = 'true'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
