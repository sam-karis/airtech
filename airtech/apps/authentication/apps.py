from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'airtech.apps.authentication'

    def ready(self):
        from . import signals  # noqa F401
