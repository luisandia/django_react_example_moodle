from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework import generics, authentication, permissions

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

