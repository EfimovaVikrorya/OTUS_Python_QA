import pytest
import requests
import csv
from files import CSV_FILE_PATH_ALL_BREWIRIES

with open(CSV_FILE_PATH_ALL_BREWIRIES, "r") as f:
    breweries = csv.reader(f)
    header = next(breweries)
    for brew in breweries:
        brews = dict(zip(header,brew))
