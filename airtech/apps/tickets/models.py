from django.db import models

from airtech.apps.authentication.models import User
from airtech.apps.flights.models import Flight
from airtech.helpers.id_generator import id_gen
from airtech.models import BaseModel


class Ticket(BaseModel):
    '''
    Handles creation of tickets
    '''
    flight = models.ForeignKey(
        Flight, related_name='tickets', on_delete=models.CASCADE)
    traveller = models.ForeignKey(
        User, related_name='tickets', on_delete=models.CASCADE)
    departure_date = models.DateField()
    seat_number = models.CharField(max_length=50)
    ticket_no = models.CharField(
        db_index=True, max_length=100, unique=True,
        default=id_gen, editable=False
    )
    status = models.CharField(max_length=50, default='Awaiting Boarding')
    notification_sent = models.BooleanField(default=False)

    class Meta:
        unique_together = (('flight', 'traveller', 'departure_date'))

    def __str__(self):
        return f'{self.flight} -> {self.traveller}'
