from django.conf.urls import url
from django.urls import path

from airtech.apps.authentication.views import (DeleteProfileImageAPIView,
                                               GetAllProfileAPIView,
                                               LoginUserAPIView,
                                               RegisterUserAPIView,
                                               SpecificUserProfileAPIView)

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),
    path('login/', LoginUserAPIView.as_view(), name='login_user'),
    path('users/profiles/', GetAllProfileAPIView.as_view(), name='profiles'),
    url(
        r'^users/profiles/(?P<username>[a-zA-Z0-9]+)$',
        SpecificUserProfileAPIView.as_view(), name='user_profile'
    ),
    path(
        'users/profiles/image/', DeleteProfileImageAPIView.as_view(),
        name='delete_image'
    ),
]
