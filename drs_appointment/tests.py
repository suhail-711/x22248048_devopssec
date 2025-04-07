import pytest
from django.urls import reverse
@pytest.mark.django_db

def test_homepage(client):
    """Unit test Case to check the redirection of home page."""
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200