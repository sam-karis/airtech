import json
import os

from faker import Faker
from locust import HttpLocust, TaskSet, task


class APIClientBehaviour(TaskSet):

    def __int__(self, parent):
        self.base_url = "/api/v1"
        self.charset = "utf-8"
        self.mimetype = "application/json"
        super(APIClientBehaviour, self).__int__(parent)

    def on_start(self):
        # Get user login token
        self.token = self.login_user()
        self.fake = Faker()

    def login_user(self):
        # login user
        data = self.client.post(
            '/api/v1/auth/login/',
            data=json.dumps({
                "email": "samkaris75@gmail.com",
                "password": "TestPass1#"}),
            headers={'Content-Type': 'application/json'}
        )
        return json.loads(data._content)['user_data']['access_token']

    @task(1)
    def index(self):
        # Test index route
        self.client.get('/')

    @task(2)
    def _login(self):
        # Test login route
        self.login_user()

    @task(2)
    def book_flight(self):
        data = {
            "departure_date": self.fake.date(),
            "seat_number": "BW12"
        }
        self.client.post(
            '/api/v1/flights/b7oio10at/tickets/',
            data=json.dumps(data),
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.token}'
            }
        )


class WebsiteUser(HttpLocust):
    host = os.getenv('LOCUST_HOST')
    task_set = APIClientBehaviour
    min_wait = 5000
    max_wait = 15000
