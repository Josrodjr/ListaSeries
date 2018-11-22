# modelos de episodios

from django.db import models
from series.models import Serie

class Espisode(models.Model):
  serie_id = models.ForeignKey(Serie, on_delete=models.CASCADE)
  episode_number = models.IntegerField()
  name = models.CharField(max_length = 25)
  plot = models.TextField()
  # rating = models.DecimalField(max_digits=2, decimal_places=2)
  rating = models.FloatField()
  release_date = models.DateField()

