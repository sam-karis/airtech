import pytest

# local import
from airtech.apps.authentication.models import Profile, User
from airtech.apps.flights.models import Flight
from airtech.apps.tickets.models import Ticket


@pytest.mark.django_db
class TestModels():

    def test_user(self, user):
        # Test user model
        assert isinstance(user, User)

    def test_user_str_method(self, user):
        # Test __str__ method in user model works
        assert str(user) == 'testuser'

    def test_profile(self, user):
        # Test profile model
        assert isinstance(user.profile, Profile)

    def test_profile_str_method(self, user):
        # Test __str__ method in profile model works
        assert str(user.profile) == 'testuser'

    def test_flight(self, flight):
        # Test flight model
        assert isinstance(flight, Flight)

    def test_flight_str_method(self, flight):
        # Test __str__ method in flight model works
        assert str(flight) == 'Nairobi - Kigali'

    def test_ticket(self, ticket):
        # Test ticket model
        assert isinstance(ticket, Ticket)

    def test_ticket_str_method(self, ticket):
        # Test __str__ method in ticket model works
        assert str(ticket) == 'Nairobi - Kigali -> testuser'
