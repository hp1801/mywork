from django.urls import path
from .views import get_latest_speed

urlpatterns = [
    path('speed/', get_latest_speed, name='get-speed'),
]
