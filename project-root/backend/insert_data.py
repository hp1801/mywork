import time
import random
from speedometer_app.models import SpeedData

def simulate_speed_data():
    while True:
        speed = random.uniform(0, 120)  # Random speed between 0 and 120
        SpeedData.objects.create(speed=speed)
        print(f"Speed recorded: {speed} km/h")
        time.sleep(1)  # Wait for 1 second
