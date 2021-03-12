from rest_framework import serializers
from enroll.models import User # type: ignore


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name','email','password']