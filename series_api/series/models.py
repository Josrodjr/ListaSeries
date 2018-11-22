# modelos de series

from django.db import models

class Serie(models.Model):
  nombre = models.CharField(max_length=25)
  # Rating solo tiene dos caracteres en los enteros y dos en los decimales
  # total_rating = models.DecimalField(max_digits=2, decimal_places=2)
  total_rating = models.FloatField()
  plot = models.TextField()
  episodes = models.IntegerField()
  seasons = models.IntegerField()
  release_date = models.DateField()