import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer


@pytest.fixture
def user_data():
    yield {
        'username': 'test',
        'email': 'test@example.com',
        'password': 'dummyPass1#',
        'confirm_password': 'dummyPass1#'
    }


@pytest.fixture
def factory():
    yield RequestFactory()


@pytest.fixture()
def user():
    yield mixer.blend('authentication.User', username='testuser')
