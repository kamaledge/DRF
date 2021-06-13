from .models import *
from rest_framework import fields, serializers

class KntPerson2Serializer(serializers.ModelSerializer):
    class Meta:
        model = KntPerson2
        fields = '__all__'