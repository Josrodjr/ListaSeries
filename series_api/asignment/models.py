from django.db import models
from series.models import Serie
from django.contrib.auth.models import User

class Assignment(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  serie_id = models.ForeignKey(Serie, on_delete=models.CASCADE)
  status = models.BooleanField(default=False)
  current_episode = models.IntegerField(default=1)