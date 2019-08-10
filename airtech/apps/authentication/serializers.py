from rest_framework import serializers

# local imports
from airtech.apps.authentication.models import User
from airtech.helpers.validators import Validators


class RegisterSerializer(serializers.ModelSerializer, Validators):
    """
    Serializer to validate user data during registration
    """

    def validate_username(self, data):
        return self.is_valid_string(data, 'Username')

    def validate_password(self, data):
        return self.is_valid_password(data)

    def validate(self, data):
        confirm_password = data.get('confirm_password', None)
        if data['password'] != confirm_password:
            raise serializers.ValidationError(
                {"Password": "Password and confirm password don't match."}
            )
        return data

    access_token = serializers.CharField(max_length=500, read_only=True)
    confirm_password = serializers.CharField(
        max_length=60, required=True, write_only=True)
    password = serializers.CharField(
        max_length=60, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'is_verified',
                  'password', 'access_token', 'confirm_password', 'created_at',
                  'updated_at'
                  ]
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        # Use the `create_user` create a new user.
        validated_data.pop('confirm_password', None)
        return User.objects.create_user(**validated_data)
