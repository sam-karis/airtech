from rest_framework.generics import ListAPIView

from airtech.apps.flights.models import Flight
from airtech.apps.flights.serializers import FlightSerializer


class GetAllFlightsAPIView(ListAPIView):
    '''
    Handle getting of Flights
    '''
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
