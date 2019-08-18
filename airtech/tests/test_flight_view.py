import pytest

from airtech.apps.flights.views import GetAllFlightsAPIView


@pytest.mark.usefixtures('flight')
@pytest.mark.django_db
class TestFlightView():

    def test_flight_view(self, factory, urls):
        # Test get flights view
        request = factory.get(urls['flight_url'])
        response = GetAllFlightsAPIView.as_view()(request)
        assert response.status_code == 200
        assert 'Nairobi' in str(response.data)
