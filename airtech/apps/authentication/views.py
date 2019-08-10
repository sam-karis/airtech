from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# local imports
from airtech.apps.authentication.serializers import RegisterSerializer


class RegisterUserAPIView(APIView):
    '''
    Handles user registration
    '''
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        message = {
            'message': 'User registered successfully.',
            'data': serializer.data
        }
        return Response(message, status.HTTP_201_CREATED)
