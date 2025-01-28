from django.urls import path
from .views import index, get_latest_speed

urlpatterns = [
    path('', index, name='index'),
    path('api/latest-speed/', get_latest_speed, name='get_latest_speed'),
]