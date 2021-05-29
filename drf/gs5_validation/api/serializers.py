from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Student

# validators # priority 1
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('FieldValue should start with R/r ')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70, validators=[starts_with_r]) # validator is called on this field
    # mutilple validators can be used by using a list.
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=70)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        print('instance name before update: ', instance.name)
        instance.name = validated_data.get('name',instance.name)
        print('instance name after update: ', instance.name)

        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

    
    
    # Field Level Validation
    # priority 2
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value


    # Object Level validation: For more than 1 field
    # priority 3
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City much be Ranchi')
        return data

            
