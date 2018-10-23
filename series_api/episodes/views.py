from django.shortcuts import render

# Create your views here.
from episodes.models import Espisode
from episodes.serializers import EpisodeSerializer
from rest_framework import generics

class EpisodeListCreate(generics.ListCreateAPIView):
  queryset = Espisode.objects.all()
  serializer_class = EpisodeSerializer