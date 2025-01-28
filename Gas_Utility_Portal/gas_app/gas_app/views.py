# gas_app/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'gas_app/home.html')  # Adjusted to point to gas_app/templates/gas_app/home.html
