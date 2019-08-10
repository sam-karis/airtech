from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexAPIView(APIView):
    '''
    Handles root directory
    '''

    def get(self, request):

        message = {
            'message': 'Welcome to Airtech API.',
        }
        return Response(message, status.HTTP_200_OK)
