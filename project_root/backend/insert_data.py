import os
import django
import random
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from speedometer_app.models import SpeedData

while True:
    speed = random.uniform(0, 120)
    SpeedData.objects.create(speed=speed)
    print(f"Inserted speed: {speed}")
    sleep(1)
