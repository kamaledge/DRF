from django.db import models
from django.db.models import fields
from .models import Singer, Song
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title','singer','duration']
        # fields = '__all__'


class SingerSerializer(serializers.ModelSerializer):
    # songssung = serializers.StringRelatedField(many=True, read_only=True) # way learnt in gs41
    songssung = SongSerializer(many=True, read_only=True) # songssung is here related_name defined in Foreign Key

    class Meta:
        model = Singer
        # fields = ['id', 'name', 'gender', 'songssung']
        fields = ['id', 'name', 'gender', 'songssung']