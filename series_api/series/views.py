from django.shortcuts import render

# Create your views here.
from series.models import Serie
from series.serializers import SerieSerializer
from rest_framework import generics

class SerieListCreate(generics.ListCreateAPIView):
  queryset = Serie.objects.all()
  serializer_class = SerieSerializer