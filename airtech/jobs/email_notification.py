from apscheduler.schedulers.background import BackgroundScheduler

from airtech.helpers.email import send_email
from airtech.helpers.tickets_notification import get_tickets_remaining_one_day


def send_ticket_notification():
    tickets = get_tickets_remaining_one_day()
    for ticket in tickets:
        email = 'samkaris75@gmail.com'
        context = {
            'username': ticket.traveller.username or email,
            'flight_name': ticket.flight.plane_category,
            'origin': ticket.flight.departure,
            'destination': ticket.flight.destination,
            'seat_number': ticket.seat_number,
            'date': ticket.departure_date,
            'time': ticket.flight.departure_time
        }
        send_email(recipients=[email], template='ticket.html', context=context)


def start():
    '''Method to start the scheduled jobs
    '''
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        send_ticket_notification, 'interval', minutes=5
    )
    scheduler.start()
