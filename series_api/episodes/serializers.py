from rest_framework import serializers
from episodes.models import Espisode

class EpisodeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Espisode
    fields = '__all__'