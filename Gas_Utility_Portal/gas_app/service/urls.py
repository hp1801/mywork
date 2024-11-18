#service_url

from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/<int:pk>/', views.track_request, name='track_request'),
    path('list/', views.request_list, name='request_list'),
    path('all/', views.view_all_requests, name='view_all_requests'),
]
