import json
import os

from typing import Union


class Config:
    def __init__(self, path):
        """
        Initialize config from json file.
        """
        self._config = dict()
        if os.path.exists(path):
            with open(path) as config_file:
                self._config = json.load(config_file)

    def _get(self, key: str, default=None) -> Union[str, bool]:
        """
        Returns var from environment or, if not present, from config.

        If not present in both returns None.
        """
        return os.environ.get(key, self._config.get(key, default))

    @property
    def secret(self) -> str:
        return self._get('DJANGO_SECRET_KEY')

    @property
    def db_url(self) -> str:
        return self._get('DATABASE_URL')

    @property
    def debug(self) -> bool:
        return self._get('DEBUG', False)
