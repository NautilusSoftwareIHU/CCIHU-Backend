from django.contrib.auth.models import AbstractUser
from django.db import models

class IHUUser(AbstractUser):
    active = models.BooleanField(default=False)
    last_password_change_request = models.DateTimeField(null=True)

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.username