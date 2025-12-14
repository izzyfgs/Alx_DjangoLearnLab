from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # CharField for password
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        # Create user using get_user_model().objects.create_user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user
