from django.apps import AppConfig


class TicketsConfig(AppConfig):
    name = 'airtech.apps.tickets'

    def ready(self):
        from airtech.jobs import email_notification

        email_notification.start()
