import pytest
from rest_framework.reverse import reverse

from .models import Company


@pytest.fixture
def defaul_data():
    return {
        'name': 'app'
    }

@pytest.mark.django_db
def test_company_create():
    Company.objects.create(name='ernie')
    assert Company.objects.count() == 1

@pytest.mark.django_db
def test_company_creating(status_code, api_client):
    url = reverse('login')
    response = api_client.post(
        url, data = default_data()
    )
    assert  response.status_code == status_code