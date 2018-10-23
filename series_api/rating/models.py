# modelos de rating

from django.db import models
from series.models import Serie

class Rating(models.Model):
  serie_id = models.ForeignKey(Serie, on_delete=models.CASCADE)
  votes = models.IntegerField()
  user_rating = models.DecimalField(max_digits=2, decimal_places=2)