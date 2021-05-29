from django.db import models
from rest_framework import fields, serializers
from .models import Location, Weather



class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    weather = serializers.HyperlinkedIdentityField(view_name='weather-detail')
    class Meta:
        model = Location
        fields = ['id', 'place', 'weather']