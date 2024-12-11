from django.db import models
from django.contrib.auth.models import User  
from django.utils.timezone import now


class UserRateLimitTypes(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., 'API Request', 'Login Attempt'
   

    def __str__(self):
        return self.name
    

class UserRateLimits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relate to a specific user
    rate_limit_type = models.ForeignKey(UserRateLimitTypes, on_delete=models.CASCADE)  # Relate to rate limit type
    request_count = models.PositiveIntegerField(default=0)  # Count of requests made
    reset_at = models.DateTimeField(default=now)  # Timestamp for when the limit resets

    def __str__(self):
        return f"{self.user} - {self.rate_limit_type.name} - {self.request_count}"