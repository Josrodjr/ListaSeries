# modelos de peliculas

from django.db import models

class Pelicula(models.Model):
  total_rating = models.DecimalField(max_digits=2, decimal_places=2)
  plot = models.TextField()
  # para introducir la duracion con formato datetime.timedelta(days =x, hours =y, seconds =z)
  duration = models.DurationField()
  release_date = models.DateField()