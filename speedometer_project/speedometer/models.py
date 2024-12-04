from django.db import models

class SpeedData(models.Model):
    speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.speed} km/h at {self.timestamp}"