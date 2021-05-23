from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Student



class StudentSerializer(serializers.ModelSerializer):

    # validators # priority 1
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('FieldValue should start with R/r ')

    name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = Student
        fields = '__all__'
    
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
        if nm.lower() == 'viru' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City much be Ranchi')
        return data

    
    # validators # priority 1
    # def starts_with_r(value):
    #     if value[0].lower() != 'r':
    #         raise serializers.ValidationError('FieldValue should start with R/r ')

            
