from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# local imports
from airtech.apps.authentication.models import Profile
from airtech.apps.authentication.serializers import (LoginSerializer,
                                                     ProfileSerializer,
                                                     RegisterSerializer)
from airtech.helpers.permissions import IsOwnerOrReadOnly
from airtech.helpers.upload_cloudinary import default_profile_url, delete_file


class RegisterUserAPIView(APIView):
    '''
    Handles user registration
    '''
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {
            'message': 'User registered successfully.',
            'user_data': serializer.data
        }
        return Response(response, status.HTTP_201_CREATED)


class LoginUserAPIView(APIView):
    '''
    Handles user login
    '''
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        response = {
            'message': 'Login is successfully.',
            'user_data': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)


class SpecificUserProfileAPIView(RetrieveUpdateAPIView):
    '''
    Handle getting a profile for specific user
    '''
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            username = self.kwargs.get('username')
            profile = Profile.objects.select_related('user').get(
                user__username=username
            )
        except Profile.DoesNotExist:
            raise NotFound(f'No profile related to {username} username')
        else:
            self.check_object_permissions(self.request, profile)
            return profile


class GetAllProfileAPIView(ListAPIView):
    '''
    Handle getting of user profiles
    '''

    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class DeleteProfileImageAPIView(APIView):
    '''
    Handle getting of user profiles
    '''

    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        profile = request.user.profile
        is_deleted = delete_file(profile.image_url)
        if is_deleted:
            profile.image_url = default_profile_url
            profile.save()
            message = 'Profile image deleted successfully and default set!!'
        else:
            message = 'No profile image to delete, default cannot be deleted!!'

        return Response({'message': message, 'data': model_to_dict(profile)})
