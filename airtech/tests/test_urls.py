from django.urls import resolve, reverse


class TestUrls():

    def test_index_url(self):
        # test index url
        path = reverse('index')
        assert path == '/'
        assert resolve(path).view_name == 'index'

    def test_register_url(self):
        # test register url
        path = reverse('authentication:register_user')
        assert path == '/api/v1/auth/register/'

    def test_login_url(self):
        # test login url
        path = reverse('authentication:login_user')
        assert path == '/api/v1/auth/login/'
