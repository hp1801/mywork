from django.urls import path
from .views import get_speed_data

urlpatterns = [
    path('data/', get_speed_data, name='get_speed_data'),
]
