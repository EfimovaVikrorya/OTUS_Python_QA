import pytest
import requests


def test_check(base_url, base_status):
    r = requests.get(base_url)
    assert r.status_code == int(base_status)
