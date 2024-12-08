from django.contrib.auth.models import AbstractUser
from django.db import models

class IHUUser(AbstractUser):
    active = models.BooleanField(default=False)
    last_password_change_request = models.DateTimeField(null=True)