from django.db import models

from airtech.helpers.id_generator import id_gen
from airtech.models import BaseModel


class Flight(BaseModel):
    '''
    Handles creation of flights
    '''
    plane_category = models.CharField(max_length=255)
    flight_no = models.CharField(
        db_index=True, max_length=100, unique=True,
        default=id_gen, editable=False
    )
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    expected_arrival_time = models.TimeField()
    capacity = models.IntegerField()
    ticket_price = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.departure} - {self.destination}'
