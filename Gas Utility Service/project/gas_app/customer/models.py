from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username






