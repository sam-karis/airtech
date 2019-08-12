from django.urls import path

from airtech.apps.authentication.views import (LoginUserAPIView,
                                               RegisterUserAPIView)

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),
    path('login/', LoginUserAPIView.as_view(), name='login_user'),
]
