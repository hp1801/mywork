from django.http import JsonResponse
from .models import SpeedData

def get_latest_speed(request):
    try:
        latest_data = SpeedData.objects.latest('timestamp')
        return JsonResponse({'speed': latest_data.speed})
    except SpeedData.DoesNotExist:
        return JsonResponse({'speed': 0})
