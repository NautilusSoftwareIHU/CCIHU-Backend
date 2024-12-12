from rest_framework import serializers
from ..models import IHUUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=IHUUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}