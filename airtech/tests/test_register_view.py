import pytest
from django.urls import reverse

from airtech.apps.authentication.views import RegisterUserAPIView


@pytest.mark.django_db
class TestRegisterView():

    register_url = reverse('authentication:register_user')

    def test_register_view_with_complete_data(self, factory, user_data):
        # Test register view
        request = factory.post(
            self.register_url, user_data,
            content_type='application/json'
        )
        response = RegisterUserAPIView.as_view()(request)
        assert response.status_code == 201
        assert 'User registered successfully.' == response.data['message']

    def test_register_view_with_incomplete_data(self, factory):
        # Test register request with incomplete data
        incomplete_data = {'username': 'test'}
        request = factory.post(
            self.register_url, incomplete_data, content_type='application/json')
        response = RegisterUserAPIView.as_view()(request)
        assert response.status_code == 400

    def test_register_view_with_invalid_email(self, factory, user_data):
        # Test registering with invalid email
        user_data['email'] = 'invalid'
        request = factory.post(
            self.register_url, user_data,
            content_type='application/json'
        )
        response = RegisterUserAPIView.as_view()(request)
        assert 'Enter a valid email address.' in str(response.data)

    def test_register_view_with_invalid_password(self, factory, user_data):
        # Test register with invalid password
        user_data['password'] = 'invalidpass'
        request = factory.post(
            self.register_url, user_data,
            content_type='application/json'
        )
        response = RegisterUserAPIView.as_view()(request)
        assert 'Password must contain a number, capital letter and special charachter' in str(  # noqa E501
            response.data)

    def test_register_view_with_unmatching_password(self, factory, user_data):
        # Test register with diff password and confirm password
        user_data['password'] = 'Pass1@wrong'
        request = factory.post(
            self.register_url, user_data,
            content_type='application/json'
        )
        response = RegisterUserAPIView.as_view()(request)
        assert "Password and confirm password don't match." in str(
            response.data)

    def test_register_view_with_invalid_username(self, factory, user_data):
        # user a username of special character only
        user_data['username'] = '####'
        request = factory.post(
            self.register_url, user_data,
            content_type='application/json'
        )
        response = RegisterUserAPIView.as_view()(request)
        assert 'Username cannot contain numbers or special characters only' in str(response.data)  # noqa E501
