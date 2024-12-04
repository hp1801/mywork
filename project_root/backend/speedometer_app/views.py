from django.http import JsonResponse
from .models import SpeedData

def get_speed_data(request):
    latest_speed = SpeedData.objects.last()
    return JsonResponse({'speed': latest_speed.speed if latest_speed else 0})
