from django import forms
from django.contrib.auth.models import User
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['account_number', 'contact_number', 'address']
