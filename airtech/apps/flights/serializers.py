from rest_framework import serializers

from airtech.apps.flights.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    """
    serializers for Flight
    """

    class Meta:
        model = Flight
        fields = (
            'plane_category', 'departure', 'destination', 'departure_time',
            'flight_no', 'expected_arrival_time', 'capacity',
            'ticket_price'
        )
