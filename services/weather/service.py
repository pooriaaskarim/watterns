from .interfaces import WttrInterface, IWeatherInterface


class WeatherService:
    def __init__(self, interface: IWeatherInterface = WttrInterface()):
        self.interface = interface
