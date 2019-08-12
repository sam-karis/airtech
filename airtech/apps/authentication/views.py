from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# local imports
from airtech.apps.authentication.serializers import (LoginSerializer,
                                                     RegisterSerializer)


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
