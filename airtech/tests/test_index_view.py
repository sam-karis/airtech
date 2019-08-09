from django.urls import reverse

from airtech.views import IndexAPIView


class TestIndexView():

    index_url = reverse('index')

    def test_index(self, factory):
        # Test index view works
        request = factory.get(self.index_url)
        response = IndexAPIView.as_view()(request)
        assert response.status_code == 200
        assert 'Welcome to Airtech API.' == response.data['message']
