from django.contrib.auth import authenticate
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed

# local imports
from airtech.apps.authentication.models import Profile, User
from airtech.helpers.upload_cloudinary import upload_file
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
        fields = ['first_name', 'last_name', 'email', 'username',
                  'is_verified', 'access_token', 'password',
                  'confirm_password', 'created_at', 'updated_at'
                  ]
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        # Use the `create_user` create a new user.
        validated_data.pop('confirm_password', None)
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """
    Serializer to validate credentials during login
    """
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    first_name = serializers.CharField(max_length=255, read_only=True)
    access_token = serializers.CharField(max_length=500, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, password=password)

        if user is None:
            raise AuthenticationFailed(
                'Invalid email or password', status.HTTP_401_UNAUTHORIZED)

        user_detail = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'access_token': user.token
        }
        return user_detail


class ProfileSerializer(serializers.ModelSerializer):
    """
    serializers for user profile
    """
    username = serializers.CharField(source='user.username', required=False)
    profile_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Profile
        fields = (
            'username', 'bio', 'image_url', 'country', 'city', 'company',
            'profile_image', 'phone', 'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at')

    def save(self):
        image = self.validated_data.pop(
            'profile_image', None) or self.validated_data.get('image_url')
        if image is not None:
            self.validated_data['image_url'] = upload_file(
                image) or self.instance.image_url
        super(ProfileSerializer, self).save()
