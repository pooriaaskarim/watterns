from services import WeatherService


def main() -> None:
    weather_service = WeatherService()
    # weather_service.interface.how_is(location='shiraz')
    weather_service.interface.get_rainy_days(location='tonekabon')


if __name__ == '__main__':
    main()
