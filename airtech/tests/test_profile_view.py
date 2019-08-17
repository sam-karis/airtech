
import mock
import pytest
from rest_framework.test import force_authenticate

from airtech.apps.authentication.views import (DeleteProfileImageAPIView,
                                               GetAllProfileAPIView,
                                               SpecificUserProfileAPIView)
from airtech.helpers.upload_cloudinary import default_profile_url, delete_file


@pytest.mark.django_db
class TestProfileView():

    url = 'https://res.cloudinary.com/samkaris/image/upload/v1566002652/airtech-v1/xihbnq9vshxjm5ish0p9.png'  # noqa E501

    def test_get_user_profiles_view(self, factory, urls, user):
        request = factory.get(urls['profile_url'])
        force_authenticate(request, user=user)
        response = GetAllProfileAPIView.as_view()(request)
        assert response.status_code == 200
        assert 'testuser' in str(response.data)

    def test_get_profiles_unauthenticated_user(self, factory, urls):
        request = factory.get(urls['profile_url'])
        response = GetAllProfileAPIView.as_view()(request)
        assert response.status_code == 403
        assert 'Authentication credentials were not provided.' in str(
            response.data)

    def test_get_specific_user_profiles_view(self, factory, urls, user):
        request = factory.get(urls['profile_user_url'])
        force_authenticate(request, user=user)
        response = GetAllProfileAPIView.as_view()(request)
        assert response.status_code == 200
        assert 'testuser' in str(response.data)

    @mock.patch('cloudinary.uploader.upload')
    def test_update_user_profiles(self, mock_, factory, urls, user, user_profile_data):  # noqa E501
        mock_.return_value = default_profile_url
        request = factory.put(
            urls['profile_user_url'], user_profile_data,
            content_type='application/json')
        force_authenticate(request, user=user)
        response = SpecificUserProfileAPIView.as_view()(
            request, username='testuser')
        assert response.status_code == 200
        assert default_profile_url in str(response.data)

    @pytest.mark.usefixtures('another_user')
    def test_update_another_user_profiles(self, factory, urls, user, user_profile_data):  # noqa E501
        request = factory.put(
            urls['profile_user_url'], user_profile_data,
            content_type='application/json')
        force_authenticate(request, user=user)
        response = SpecificUserProfileAPIView.as_view()(
            request, username='another_user')
        assert response.status_code == 403
        assert 'You do not have permission to perform this action' in str(
            response.data)

    @mock.patch('airtech.apps.authentication.views.delete_file')
    def test_delete_user_profiles_image(self, mock_, factory, urls, user):
        mock_.return_value = True
        request = factory.delete(urls['profile_image_url'])
        force_authenticate(request, user=user)
        response = DeleteProfileImageAPIView.as_view()(request)
        assert 'Profile image deleted successfully and default set!!' == response.data[  # noqa E501
            'message']

    @mock.patch('airtech.apps.authentication.views.delete_file')
    def test_delete_non_existing_user_profiles_image(self, mock_, factory, urls, user):  # noqa E501
        mock_.return_value = False
        request = factory.delete(urls['profile_image_url'])
        force_authenticate(request, user=user)
        response = DeleteProfileImageAPIView.as_view()(request)
        assert 'No profile image to delete, default cannot be deleted!!' == response.data[  # noqa E501
            'message']

    @mock.patch('cloudinary.uploader.destroy')
    def test_delete_file_function(self, mock_):
        mock_.return_value = {'result': 'ok'}
        response = delete_file(self.url)
        assert response is True

    @mock.patch('cloudinary.uploader.destroy')
    def test_delete_file_function_non_existing_file(self, mock_):
        mock_.side_effect = Exception
        response = delete_file(self.url)
        assert response is False
