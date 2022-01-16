from re import T
from rest_framework import viewsets

from django.contrib.auth.models import User
from .serializers import UserSerializer
#to make password encryption
from django.contrib.auth.hashers import make_password

#API view for django.contrib.auth.models.User
class UserViewSet(viewsets.ModelViewSet):
  queryset=User.objects.all()
  serializer_class=UserSerializer

  #it takes recent instance from serializer and user 'make_password' to encrypt password
  def perform_create(self, serializer):
    if('password' in self.request.data):
      password=self.request.data['password']
      password=make_password(password)
      serializer.save(password=password)
    else:
      serializer.save()
  
  def perform_update(self, serializer):
    # Hash password if it is provided
    if('password' in self.request.data):
      password=self.request.data['password']
      password=make_password(password)
      serializer.save(password=password)  # Hash password if it is provided
    else:
      serializer.save()
