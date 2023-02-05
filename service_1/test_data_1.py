import pytest
import requests
import json
from files import JSON_FILE_PATH_ALL_BREEDS

with open(JSON_FILE_PATH_ALL_BREEDS, "r") as f:
    breeds = json.loads(f.read())
