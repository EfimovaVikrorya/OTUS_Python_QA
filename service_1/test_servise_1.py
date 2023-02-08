import pytest
import requests
import conftest
from test_data_1 import breeds


@pytest.mark.regression
def test_all_breed_status_success():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    assert r.status_code == 200
    assert r.json()['status'] == 'success'


@pytest.mark.regression
def test_all_breed_format_json():
    r = requests.get('https://dog.ceo/api/breeds/list/all')
    assert r.json() == breeds


@pytest.mark.regression
def test_sub_breed_status_success():
    r = requests.get('https://dog.ceo/api/breed/hound/list')
    assert r.status_code == 200
    assert r.json()['status'] == 'success'


@pytest.mark.regression
@pytest.mark.parametrize('param', ['hound', 'terrier', 'spaniel'])
def test_sub_breed_format_json(param):
    r = requests.get('https://dog.ceo/api/breed/' + param + '/list')
    r_json = r.json()
    print(r_json['message'][param])
    assert breeds['message'][param] == r_json['message'][param]


@pytest.mark.regression
def test_sub_breed_status_success():
    r = requests.get('https://dog.ceo/api/breed/hound/images')
    assert r.status_code == 200
    assert r.json()['status'] == 'success'


@pytest.mark.regression
@pytest.mark.parametrize('param', ['malamute', 'pomeranian', 'wolfhound'])
def test_breed_foto(param):
    r = requests.get('https://dog.ceo/api/breed/' + param + '/images')
    r_json = r.json()
    print(r_json['message'])
    assert len(list(breeds['message'])) > 0
