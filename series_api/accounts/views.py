from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

class UserCreate(APIView):
  # Permitir a cualquiera acceder a esta view
  permission_classes = (AllowAny,)
  # create the user
  def post(self, request, format='json'):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      if user:
        return Response(serializer.data, status=status.HTTP_201_CREATED)