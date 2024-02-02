import requests

from services.weather.interfaces.i_weather_interface import IWeatherInterface
from .models.location_weather import *
import json


class WttrInterface(IWeatherInterface):
    def __init__(self):
        super().__init__(api_base='https://wttr.in/')

    def how_is(self, location: str, locale: str or None = None) -> None:
        try:
            response = requests.get(
                f'{self.api_base}{location}',
                headers={'accept-language': locale}, )
            print(response.text)
        except Exception as e:
            print(f'Sh$%t Happened\n\t{e}')

    def get_rainy_days(self, location: str, locale: str or None = None):
        response = requests.get(
            f'{self.api_base}{location}?format=j1',
            headers={'accept-language': locale},
        )
        data = json.loads(response.text)
        wttr = Wttr.from_dict(data)
        days = [weather for weather in wttr.weather]
        probable_rainy_days = filter(
            lambda day: any(int(hourly.chanceofrain) > 0 for hourly in day.hourly), days)

        new_line = '\n'
        tab = '\t'

        print(f"""
{location.capitalize()}:{tab.join(
            [
                f'{new_line}{tab}{rainy_day.date}:{new_line}{tab}{tab}'
                + f'{new_line}{tab}{tab}'.join(
                    [
                        f'Raining chance of %{hour.chanceofrain.ljust(3, " ")}'
                        f' at {hour.time.rjust(4, "0")[:2]}:00'
                        for hour in rainy_day.hourly if int(hour.chanceofrain) > 0
                    ]
                )
                for rainy_day in probable_rainy_days
            ]
        )
        }
""")
