import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)

CSV_FILE_PATH_ALL_BREWIRIES = get_path(filename="breweries.csv")
