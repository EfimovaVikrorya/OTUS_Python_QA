import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)

JSON_FILE_PATH_ALL_BREEDS = get_path(filename="all_breeds.json")
