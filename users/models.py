# users/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     age = models.PositiveIntegerField(null=True, blank=True)

class Customer(models.Model):
    # username = ?
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=10)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(null=True, max_length=14)

    def __str__(self):
        return self.customer_id