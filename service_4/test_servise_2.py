import pytest
import requests


@pytest.mark.regression
@pytest.mark.parametrize('city,city_name,state_name', [
    ('san_diego', 'San Diego', 'California'),
    ('denver', 'Denver', 'Colorado'),
    ('clovis', 'Clovis', 'California')
])
def test_filter_breweries_by_city(city, city_name, state_name):
    r = requests.get('https://api.openbrewerydb.org/breweries?by_city=' + city + '&per_page=3')
    assert r.status_code == 200
    for i in r.json():
        assert i['city'] == city_name
        assert i['state'] == state_name


@pytest.mark.regression
@pytest.mark.parametrize('state,state_name', [
    ('new_york', 'New York')
])
def test_filter_breweries_by_state(state, state_name):
    r = requests.get('https://api.openbrewerydb.org/breweries?by_state=' + state + '&per_page=3')
    assert r.status_code == 200
    for i in r.json():
        assert i['state'] == state_name


@pytest.mark.regression
def test_meta_data():
    r = requests.get('https://api.openbrewerydb.org/breweries/meta')
    assert r.status_code == 200
    assert r.json()["total"] == "8170"
    assert r.json()["page"] == "1"
    assert r.json()["per_page"] == "20"


@pytest.mark.regression
def test_autocomplete():
    r = requests.get('https://api.openbrewerydb.org/breweries/autocomplete?query={dog}')
    assert r.status_code == 200
    for row in r.json():
        assert 'Dog' in row["name"]


@pytest.mark.regression
def test_random_breweries():
    r = requests.get('https://api.openbrewerydb.org/breweries/random?size=3')
    assert r.status_code == 200
    assert len(r.json()) == 3


