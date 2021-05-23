from rest_framework import serializers

class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField(default=None)
    city = serializers.CharField(max_length=100)