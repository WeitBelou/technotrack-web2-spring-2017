import json
from os import environ


class Config:
    def __init__(self, path):
        """
        Initialize config from json file.
        """
        with open(path) as config_file:
            self._config = json.load(config_file)

    def _get(self, key: str) -> [str, bool]:
        """
        Returns var from environment or, if not present, from config.

        If not present in both returns None.
        """
        return environ.get(key, self._config.get(key))

    @property
    def secret(self) -> str:
        return self._get('DJANGO_SECRET')

    @property
    def db_url(self) -> str:
        return self._get('DATABASE_URL')

    @property
    def debug(self) -> bool:
        return self._get('DEBUG')
