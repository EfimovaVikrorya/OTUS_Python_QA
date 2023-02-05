import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://dog.ceo/api/breeds/image/random"