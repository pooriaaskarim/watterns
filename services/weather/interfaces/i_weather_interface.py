from abc import (
    ABCMeta,
    abstractmethod,
)
from requests import Response


class IWeatherInterface(metaclass=ABCMeta):

    def __init__(self, api_base: str):
        self.api_base = api_base

    @abstractmethod
    def how_is(self, location: str, locale: str or None = None) -> None:
        pass

    @abstractmethod
    def get_rainy_days(self, location: str) -> Response:
        pass
