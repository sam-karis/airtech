from datetime import date, datetime, timedelta

from airtech.apps.tickets.models import Ticket


def get_tickets_remaining_one_day():
    # Get all tickets remaing less than 24 hours
    yesterday = date.today() - timedelta(days=1)
    all_awaiting_tickets = Ticket.objects.filter(
        notification_sent=False, status='Awaiting Boarding',
        departure_date__gte=yesterday
    )
    tickets_to_send_notification = []
    for ticket in all_awaiting_tickets:
        ticket_date = ticket.departure_date
        flight_time = ticket.flight.departure_time
        date_time = datetime.combine(ticket_date, flight_time)
        remaining_time = abs(date_time - datetime.now())
        remaining_hours = remaining_time.total_seconds() / 3600.0
        if remaining_hours <= 24:
            tickets_to_send_notification.append(ticket)
            ticket.notification_sent = True
            ticket.save()
    return tickets_to_send_notification
