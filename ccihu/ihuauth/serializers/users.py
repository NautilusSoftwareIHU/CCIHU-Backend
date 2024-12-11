from rest_framework import serializers
from ..models import IHUUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=IHUUser
        fields = ('active','last_password_change_request')