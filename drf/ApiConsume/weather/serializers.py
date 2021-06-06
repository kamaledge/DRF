from django.db import models
from rest_framework import fields, serializers
from .models import Location, Weather



class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    weathers = serializers.HyperlinkedRelatedField(view_name='app_name:weather-detail', read_only=True)
    class Meta:
        model = Location
        fields = ['id', 'place', 'weathers']