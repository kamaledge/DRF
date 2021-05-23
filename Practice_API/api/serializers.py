from django.db.models import fields
from rest_framework import serializers
from .models import Traveller

class TravellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Traveller
        fields = '__all__'