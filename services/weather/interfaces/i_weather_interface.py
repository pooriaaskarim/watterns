from abc import (
    ABCMeta,
    abstractmethod,
    abstractproperty,
)
import requests
from requests import Response


class IWeatherApi(metaclass=ABCMeta):
    def __init__(self, api_base: str):
        self.api_base = api_base

    def how_is(self, location: str) -> str:
        """returns Api to retrieve weather information in a Displayable"""
        pass

    def get(self, location: str) -> str:
        """returns Api to retrieve weather information in Json Format"""
        pass


class IWeatherInterface(metaclass=ABCMeta):

    def __init__(self, api: IWeatherApi, locale: str = 'en'):
        self.api = api
        self.locale = locale

    @abstractmethod
    def how_is(self, location: str, locale: str or None = None) -> None:
        response = requests.get(self.api.how_is(location=location),
                                headers={'accept-language': self.locale if not locale else locale},
                                )
        print(response.text)

    @abstractmethod
    def get(self, location: str) -> Response:
        return requests.get(
            self.api.get(location=location),
            headers={'accept-language': self.locale},
            )
