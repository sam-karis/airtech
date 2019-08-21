from django.urls import path

from airtech.apps.tickets.views import TicketAPIView, TicketCountAPIView

app_name = 'ticket'

urlpatterns = [
    path('<flight_no>/tickets/', TicketAPIView.as_view(), name='tickets'),
    path('<flight_no>/', TicketCountAPIView.as_view(), name='tickets_count'),
]
