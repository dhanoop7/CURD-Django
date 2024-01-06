
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
   
    pass


class Car(models.Model):
    brand = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.number})"
