import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from airtech.apps.authentication.views import RegisterUserAPIView
from airtech.helpers.upload_cloudinary import default_profile_url


@pytest.fixture
def factory():
    yield RequestFactory()


@pytest.fixture
def urls():
    yield {
        'index_url': reverse('index'),
        'register_url': reverse('authentication:register_user'),
        'login_url': reverse('authentication:login_user'),
        'profile_url': reverse('authentication:profiles'),
        'profile_user_url': reverse(
            'authentication:user_profile', kwargs={'username': 'testuser'}),
        'profile_image_url': reverse('authentication:delete_image'),
        'flight_url': reverse('flight:flights'),
        'ticket_url': reverse(
            'tickets:tickets', kwargs={'flight_no': 'fn-aeiph89oy'}),
        'ticket_count_url': reverse(
            'tickets:tickets_count', kwargs={'flight_no': 'fn-aeiph89oy'}),

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


@pytest.fixture()
def another_user():
    yield mixer.blend(
        'authentication.User', username='another_user',
        email='another_user@example.com', password='dummyPass1#'
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


@pytest.fixture
def user_profile_data():
    yield {
        'country': 'Kenya',
        'city': 'Nairobi',
        'image_url': default_profile_url,
        'company': 'Andela Kenya'
    }


@pytest.fixture()
def flight():
    yield mixer.blend(
        'flights.Flight', departure='Nairobi', destination='Kigali',
        flight_no='fn-aeiph89oy'
    )


@pytest.fixture()
def ticket(flight, user):
    yield mixer.blend(
        'tickets.Ticket', flight=flight, traveller=user,
        departure_date='2019-08-29', ticket_no='tk-aeiph89oy'
    )


@pytest.fixture
def ticket_data():
    yield {'departure_date': '2019-09-29', 'seat_number': 'W23'}
