from django.shortcuts import render

# Create your views here.
from peliculas.models import Pelicula
from peliculas.serializers import PeliculaSerializer
from rest_framework import generics

class PeliculaListCreate(generics.ListCreateAPIView):
  queryset = Pelicula.objects.all()
  serializer_class = PeliculaSerializer