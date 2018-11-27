from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from series.models import Serie
from series.serializers import SerieSerializer
from rest_framework import generics

class SerieListCreate(generics.ListCreateAPIView):
  queryset = Serie.objects.all()
  serializer_class = SerieSerializer


class SeriesList(generics.ListAPIView):
  serializer_class = SerieSerializer

  def get_queryset(self):
    seriename = self.kwargs['serie_name']
    return Serie.objects.filter(name__icontains=seriename)