from django.utils.dateparse import parse_date
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from airtech.apps.flights.models import Flight
from airtech.apps.tickets.models import Ticket
from airtech.apps.tickets.serializers import TicketSerializer


class TicketBaseAPIView(APIView):

    def get_flight(self):
        flight_no = self.kwargs.get('flight_no')
        flight = Flight.objects.filter(flight_no=flight_no).first()
        if not flight:
            raise NotFound(f'No flight related to {flight_no} flight number.')
        else:
            return flight


class TicketAPIView(TicketBaseAPIView):
    '''
    Handles booking of flight tickets and individual tickets
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def post(self, request, **kwargs):
        request.data['flight'] = self.get_flight().pk
        request.data['traveller'] = request.user.pk
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {
            'message': 'You have successfully booked a flight.',
            'ticket_data': serializer.data
        }
        return Response(response, status.HTTP_201_CREATED)

    def get(self, request, **kwargs):
        flight = self.get_flight()
        queryset = Ticket.objects.filter(
            traveller=self.request.user, flight=flight)
        serializer = self.serializer_class(queryset, many=True)
        message = {'count': queryset.count(), 'tickets': serializer.data}
        return Response(message, status.HTTP_200_OK)


class TicketCountAPIView(TicketBaseAPIView):
    '''
    Handles filtering tickets by date of flight tickets
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketSerializer

    def get(self, request, **kwargs):
        flight = self.get_flight()
        queryset = Ticket.objects.filter(flight=flight)
        if request.query_params:
            date = request.query_params.get('date')
            if parse_date(date):
                queryset = queryset.filter(departure_date=date)
        serializer = self.serializer_class(queryset, many=True)
        message = {'count': queryset.count(), 'tickets': serializer.data}
        return Response(message, status.HTTP_200_OK)
