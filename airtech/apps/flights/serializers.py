from rest_framework import serializers

from airtech.apps.flights.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    """
    serializers for Flight
    """

    available_seats = serializers.IntegerField(read_only=True)
    available_status = serializers.CharField(max_length=50, read_only=True)

    class Meta:
        model = Flight
        fields = (
            'plane_category', 'departure', 'destination', 'departure_time',
            'expected_arrival_time', 'capacity', 'booked_seats',
            'ticket_price', 'available_seats', 'available_status',
        )
        read_only_fields = ('available_seats', 'available_status')
