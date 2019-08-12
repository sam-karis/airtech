import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from airtech.apps.authentication.views import RegisterUserAPIView


@pytest.fixture
def factory():
    yield RequestFactory()


@pytest.fixture
def urls():
    yield {
        'register_url': reverse('authentication:register_user'),
        'login_url': reverse('authentication:login_user')
    }


@pytest.fixture
def user_data():
    yield {
        'username': 'test',
        'email': 'test@example.com',
        'password': 'dummyPass1#',
        'confirm_password': 'dummyPass1#'
    }


@pytest.fixture()
def user():
    yield mixer.blend(
        'authentication.User', username='testuser',
        email='test2@example.com', password='dummyPass1#'
    )


@pytest.fixture
def user_login_data():
    yield {'email': 'test@example.com', 'password': 'dummyPass1#'}


@pytest.fixture
def invalid_login_data():
    yield {'email': 'test@example.com', 'password': 'wrongPass'}


@pytest.fixture
def register_user(factory, urls, user_data):
    request = factory.post(
        urls['register_url'], user_data,
        content_type='application/json'
    )
    yield RegisterUserAPIView.as_view()(request)
