from django.urls import reverse, resolve


class TestUrls():

    def test_index_url(self):
        # test index url
        path = reverse('index')
        assert path == '/'
        assert resolve(path).view_name == 'index'

    def test_register_url(self):
        # test register url
        path = reverse('authentication:register_user')
        assert path == '/api/users/register/'
