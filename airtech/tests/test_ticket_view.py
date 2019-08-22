import pytest
from rest_framework.test import force_authenticate

from airtech.apps.tickets.views import TicketAPIView, TicketCountAPIView


@pytest.mark.usefixtures('ticket')
@pytest.mark.django_db
class TestTicketView():

    def test_get_traveller_ticket_view(self, factory, urls, user):
        # Test get a traveller tickets view
        request = factory.get(urls['ticket_url'])
        force_authenticate(request, user=user)
        response = TicketAPIView.as_view()(request, flight_no='fn-aeiph89oy')
        assert response.status_code == 200
        assert 'seat_number' in str(response.data)

    def test_get_ticket_non_existing(self, factory, urls, user):
        # Test get a traveller tickets view
        request = factory.get(urls['ticket_url'])
        force_authenticate(request, user=user)
        response = TicketAPIView.as_view()(request, flight_no='fn-wrong')
        assert 'No flight related to fn-wrong flight number.' in str(
            response.data)

    def test_booking_a_ticket_date(self, factory, urls, ticket_data, user):
        # Test booking a ticket
        request = factory.post(
            urls['ticket_url'], ticket_data, content_type='application/json')
        force_authenticate(request, user=user)
        response = TicketAPIView.as_view()(request, flight_no='fn-aeiph89oy')
        assert response.status_code == 201
        assert 'You have successfully booked a flight.' == response.data.get(
            'message')

    def test_ticket_count_by_date(self, factory, urls, user):
        # Test a count for all tickets in a day
        url = f"{urls['ticket_count_url']}?date=2019-08-29"
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = TicketCountAPIView.as_view()(
            request, flight_no='fn-aeiph89oy')
        assert response.status_code == 200
        assert 1 == response.data['count']
