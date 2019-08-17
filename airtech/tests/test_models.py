import pytest

# local import
from airtech.apps.authentication.models import Profile, User
from airtech.apps.flights.models import Flight


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

    def test_flights(self, flight):
        # Test flight model
        assert isinstance(flight, Flight)

    def test_flight_str_method(self, flight):
        # Test __str__ method in profile model works
        assert str(flight) == 'Nairobi - Kigali'
