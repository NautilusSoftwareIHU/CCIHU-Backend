from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import IHUUser

# Create your views here.
class IhuUserView(generics.CreateAPIView):
    queryset = IHUUser.objects.all()
    serializer_class = UserSerializer