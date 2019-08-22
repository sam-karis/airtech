from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from airtech.apps.tickets.models import Ticket
from airtech.apps.flights.serializers import FlightSerializer


class TicketSerializer(serializers.ModelSerializer):
    """
    serializers for Ticket
    """
    flight_details = FlightSerializer(
        source='flight', read_only=True, required=False)

    class Meta:
        model = Ticket
        fields = (
            'flight', 'traveller', 'departure_date', 'ticket_no',
            'seat_number', 'created_at', 'updated_at', 'flight_details'
        )
        read_only_fields = ('ticket_no', 'created_at', 'updated_at',)
        validators = [
            UniqueTogetherValidator(
                queryset=Ticket.objects.all(),
                fields=['flight', 'traveller', 'departure_date']
            )
        ]
