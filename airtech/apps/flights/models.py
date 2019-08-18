from django.db import models

from airtech.models import BaseModel


class Flight(BaseModel):
    '''
    Handles creation of flights
    '''
    plane_category = models.CharField(max_length=255)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    expected_arrival_time = models.DateTimeField()
    capacity = models.IntegerField()
    booked_seats = models.IntegerField(default=0)
    ticket_price = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.departure} - {self.destination}'

    @property
    def available_seats(self):
        return self.capacity - self.booked_seats

    @property
    def available_status(self):
        is_available = self.available_seats >= 1
        return 'Available' if is_available else 'Not Available'
