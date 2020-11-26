# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # interesting to note:
    # -> with "null=True" can store a database entry as NULL, meaning no value
    # -> "blank=True" is db related, with this setting, a form will allow an empty value,
    #     whereas if "blank=False" then a value is required.
    # In practice, null and blank are commonly used together in this fashion
    # so that a form allows an empty value and the database stores that value as NULL.
    age = models.PositiveIntegerField(null=True, blank=True)