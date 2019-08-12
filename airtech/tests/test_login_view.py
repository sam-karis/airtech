import pytest

from airtech.apps.authentication.views import LoginUserAPIView


@pytest.mark.usefixtures('register_user')
@pytest.mark.django_db
class TestLoginView():

    def test_login_view(self, factory, urls, user_login_data):
        request = factory.post(
            urls['login_url'], user_login_data,
            content_type='application/json'
        )
        response = LoginUserAPIView.as_view()(request)
        assert response.status_code == 200
        assert 'Login is successfully.' == response.data['message']

    def test_invalid_login(self, factory, urls, invalid_login_data):
        request = factory.post(
            urls['login_url'], invalid_login_data,
            content_type='application/json'
        )
        response = LoginUserAPIView.as_view()(request)
        assert 'Invalid email or password' in str(response.data)
