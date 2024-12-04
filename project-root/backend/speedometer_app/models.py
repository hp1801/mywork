from django.db import models

class SpeedData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    speed = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - {self.speed}"

