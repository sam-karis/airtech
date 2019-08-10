from django.urls import path

from airtech.apps.authentication.views import RegisterUserAPIView

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),
]
