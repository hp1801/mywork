from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only
from .forms import CustomerRegistrationForm
from service.models import Service  # Import the Service model
from .models import Customer


# Registration view
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        customer_form = CustomerRegistrationForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()  # Save user first
            customer = customer_form.save(commit=False)  # Don't save customer yet
            customer.user = user  # Associate user with customer
            customer.save()  # Now save the customer
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the profile or another page after successful registration
    else:
        user_form = UserCreationForm()
        customer_form = CustomerRegistrationForm()

    return render(request, 'customer/register.html', {'user_form': user_form, 'customer_form': customer_form})

# Profile view (for regular users)
@login_required


def profile(request):
    return render(request, 'customer/profile.html', {'user': request.user})

# Login view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Logout view
def logout_user(request):
    logout(request)
    return redirect('/')  # Redirect to home after logout


@login_required
@admin_only
def all_requests(request):
    # Fetch all service requests
    requests = Service.objects.all()
    return render(request, 'service/view_all_requests.html', {'requests': requests})
