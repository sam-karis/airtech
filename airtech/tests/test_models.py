import pytest

# local import
from airtech.apps.authentication.models import User


@pytest.mark.django_db
class TestModels():

    def test_user(self, user):
        # Test user model
        assert isinstance(user, User)

    def test_str_method(self, user):
        # Test __str__ method in user model works
        assert str(user) == 'testuser'
