from http import HTTPStatus
from django.urls import reverse
from pytest_django.asserts import assertRedirects
import pytest


# Указываем в фикстурах встроенный клиент.
def test_home_availability(client):
    # Адрес страницы получаем через reverse():
    url = reverse('metcast:create')
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_detail_availability(client, city):
    response = client.get(reverse('metcast:detail', kwargs={'city': 'City'}))
    assert response.status_code == HTTPStatus.OK
