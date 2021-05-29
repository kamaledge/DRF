from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # way 1
    # name = serializers.CharField(read_only=True) 
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # fields = '__all__'

        # way 2:
        # read_only_fields = ['name', 'roll']

        # way 3
        extra_kwargs = {'name': {'read_only': True}}


# Using Model Serializer we don't need to create create and update methods here



# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     roll = serializers.IntegerField()
#     city = serializers.CharField()

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # return super().update(instance, validated_data)
#         print('instance name before update: ', instance.name)
#         instance.name = validated_data.get('name',instance.name)
#         print('instance name after update: ', instance.name)

#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance
