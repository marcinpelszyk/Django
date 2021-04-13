import pytest
import pytz
from faker import Faker

from showtimes.models import Cinema, Screening
from .utils import fake_cinema_data, fake_screening_data
from ...moviebase.settings import TIME_ZONE
from ...movielist.models import Movie

faker = Faker("pl_PL")

TZ = pytz.timezone(TIME_ZONE)

@pytest.mark.django_db
def test_add_cinema(client, set_up):
    cinemas_before = Cinema.obejcts.count()
    new_cinema = fake_cinema_data()
    response = client.post('/cinemas/', new_cinema, format='json')
    assert response.status_code == 201
    assert Cinema.objects.count() == cinemas_before + 1

    for key, value in new_cinema.items():
        assert key in response.data
        if isinstance(value, str):
            assert len(response.data[key]) == len(value)
        else:
            assert response.data[key] == value


@pytest.mark.django_db
def test_get_cinema_list(client, set_up):
    response = client.get('/cinemas/', {}, format='json')

    assert response.status_code == 200
    assert Cinema.objects.count() == len(response.data)

@pytest.mark.django_db
def test_get_cinema_detail(client, set_up):
    cinema = Cinema.objects.first()
    resp = client.get(f'cinema/{cinema.pk}', {}, format='json')

    assert resp.status_code == 200
    for filed in ('name', 'city', 'capacity', 'movies'):
        assert filed in resp.data


@pytest.mark.django_db
def test_delete_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.delete(f'/cinema/{cinema.pk}/', {}, format='json')
    assert response.status_code == 204
    cinema_pks = [cinema.pk for cinema in Cinema.objects.all()]
    assert cinema.pk not in cinema_pks


@pytest.mark.django_db
def test_update_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f'/cinema/{cinema.pk}/', {}, format='json')
    cinema_data = response.data
    new_name = 'Helios'
    cinema_data['name'] = new_name
    new_city = 'Bialystok'
    cinema_data['city'] = new_city
    response = client.patch(f'/cinema/{cinema.pk}/', cinema_data, format='json')
    assert response.status_code == 200
    cinema_obj = Cinema.objects.get(pk=cinema.pk)
    assert cinema_obj.name == new_name
    assert cinema_obj.city == new_city


@pytest.mark.django_db
def test_add_screening(client, set_up):
    screenings_count = Screening.objects.count()
    new_screening_data = {
        "cinema": Cinema.objects.first().name,
        "movie": Movie.objects.first().title,
        "date": faker.date_time(tzinfo=TZ).isoformat()
    }
    resp = client.post('/screening/', new_screening_data, format='json')

    assert resp.status_code == 201
    assert Screening.objects.count() == screenings_count + 1

    for key, value in screenings_count.items():
        assert key in resp.data
        if isinstance(value, str):
            assert len(resp.data[key]) == len(value)
        else:
            assert resp.data[key] == value


@pytest.mark.django_db
def test_get_screening_list(client, set_up):
    resp = client.get('/screening/', {}, format='json')

    assert resp.status_code == 200
    assert Screening.objects.count() == len(resp.data)


@pytest.mark.django_db
def test_get_screening_detail(client, set_up):
    screening = Screening.objects.first()
    resp = client.get(f'/screening/{screening.pk}/', {}, format='json')

    assert resp.status_code == 200
    for filed in ('movie', 'cinema', 'date'):
        assert filed in resp.data


@pytest.mark.django_db
def test_delete_screening(client, set_up):
    screening = Screening.objects.first()
    resp = client.get(f'/screening/{screening.pk}/', {}, format='json')

    assert resp.status_code == 204
    screening_pks = [screening.pk for screening in Screening.objects.all()]
    assert screening.pk not in screening_pks