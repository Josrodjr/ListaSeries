from django.shortcuts import render

# Create your views here.
from rating.models import Rating
from rating.serializers import RatingSerializer
from rest_framework import generics

class RatingListCreate(generics.ListCreateAPIView):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer