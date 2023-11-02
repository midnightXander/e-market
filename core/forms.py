from django import forms
from .models import Order_details

class Order_details_form(forms.ModelForm):
    location = forms.CharField()
    date_of_delivery = forms.DateTimeField()
    balance = forms.IntegerField()
    
    
    class Meta:
        model = Order_details
        fields = ['location','date_of_delivery','balance']
        labels={'text':'','date':''}
