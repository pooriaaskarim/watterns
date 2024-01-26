from services.weather.interfaces.i_weather_interface import IWeatherInterface, IWeatherApi
from .models.location_weather import *
import json
from types import SimpleNamespace


class WttrApi(IWeatherApi):
    def __init__(self):
        super().__init__('https://wttr.in/')

    def how_is(self, location: str) -> str:
        return f'{self.api_base}{location}'

    def get(self, location: str) -> str:
        return f'{self.api_base}{location}0?format=j1'


class WttrInterface(IWeatherInterface):
    def __init__(self):
        super().__init__(api=WttrApi())

    def how_is(self, location: str, locale: str or None = None) -> None:
        super().how_is(location=location, locale=locale)

    def get(self, location: str):
        data = super().get(location)
        x = json.loads(data.text)
        wttr = Wttr.from_dict(x)
        probableRainyDays = []
        for w in wttr.weather:
            for h in w.hourly:
                print(w.date + '/' + h.time + '\t\t\t -----> ' + h.chanceofrain + ' : ' + [f'{desc.value}' for desc in h.weatherDesc].__str__())
                if int(h.chanceofrain) > 0:
                    probableRainyDays.append(
                        {f'{w.date}/{h.time}:{h.time}': h.chanceofrain})

        print(probableRainyDays)
