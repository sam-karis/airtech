from django.urls import resolve


class TestUrls():

    def test_index_url(self, urls):
        # test index url
        path = urls['index_url']
        assert path == '/'
        assert resolve(path).view_name == 'index'

    def test_register_url(self, urls):
        # test register url
        path = urls['register_url']
        assert path == '/api/v1/auth/register/'

    def test_login_url(self, urls):
        # test login url
        path = urls['login_url']
        assert path == '/api/v1/auth/login/'

    def test_profile_url(self, urls):
        # test profile url
        path = urls['profile_url']
        assert path == '/api/v1/auth/users/profiles/'

    def test_user_profile_url(self, urls):
        # test profile user url
        path = urls['profile_user_url']
        assert path == '/api/v1/auth/users/profiles/testuser'

    def test_profile_image_url(self, urls):
        # test profile image url
        path = urls['profile_image_url']
        assert path == '/api/v1/auth/users/profiles/image/'

    def test_flights_url(self, urls):
        # test flights url
        path = urls['flight_url']
        assert path == '/api/v1/flights/'

    def test_tickets_url(self, urls):
        # test book tickets url
        path = urls['ticket_url']
        assert path == '/api/v1/flights/fn-aeiph89oy/tickets/'

    def test_tickets_count_url(self, urls):
        # test book tickets url
        path = urls['ticket_count_url']
        assert path == '/api/v1/flights/fn-aeiph89oy/'
