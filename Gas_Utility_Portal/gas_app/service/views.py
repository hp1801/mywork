from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service
from customer.decorators import admin_only

@login_required
def submit_request(request):
    # Check if the user has a customer object associated
    if not hasattr(request.user, 'customer'):
        return redirect('customer:profile')  # Or any page that allows them to create a customer

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.customer = request.user.customer
            service.save()
            return redirect('service:request_list')
    else:
        form = ServiceForm()
    return render(request, 'service/submit_request.html', {'form': form})


@login_required
def track_request(request, pk):
    service = get_object_or_404(Service, pk=pk, customer=request.user.customer)
    return render(request, 'service/track_request.html', {'service': service})

@login_required
def request_list(request):
    if not hasattr(request.user, 'customer'):
        return redirect('customer:profile')  # Ensure that user has a customer object
    services = Service.objects.filter(customer=request.user.customer)
    return render(request, 'service/request_list.html', {'services': services, 'no_requests': not services})

@login_required
@admin_only  # Applying the decorator to restrict to admin users
def view_all_requests(request):
    requests = Service.objects.all()  # Get all service requests
    return render(request, 'service/view_all_requests.html', {'requests': requests})
