import random
import threading
import time
from django.shortcuts import render
from django.http import JsonResponse
from .models import SpeedData

# Background task to generate random speed data every second
def generate_speed_data():
    while True:
        speed = random.uniform(0, 120)  # Random speed between 0 and 120 km/h
        SpeedData.objects.create(speed=speed)
        time.sleep(1)  # Wait for 1 second before generating the next speed

# Start the background thread when the server starts
threading.Thread(target=generate_speed_data, daemon=True).start()

def index(request):
    speeds = SpeedData.objects.all().order_by('-timestamp')[:10]  # Get latest 10 records
    return render(request, 'speedometer/index.html', {'speeds': speeds})

def get_latest_speed(request):
    latest_speed = SpeedData.objects.last()  # Get the latest recorded speed
    if latest_speed:
        return JsonResponse({'speed': latest_speed.speed})
    return JsonResponse({'speed': 0})  # Return 0 if no data is available