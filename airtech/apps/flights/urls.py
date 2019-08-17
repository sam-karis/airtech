from django.urls import path

from airtech.apps.flights.views import GetAllFlightsAPIView

app_name = 'flight'

urlpatterns = [
    path('flights/', GetAllFlightsAPIView.as_view(), name='flights'),
]
