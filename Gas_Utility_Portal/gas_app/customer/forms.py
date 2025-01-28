from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['account_number', 'contact_number', 'address']
        exclude = ['user']
