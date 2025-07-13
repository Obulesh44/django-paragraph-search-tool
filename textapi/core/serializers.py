from rest_framework import serializers
from .models import User

# Serializer for the custom User model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'dob', 'password']

# Override the default create method to use our custom create_user logic

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
