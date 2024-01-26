from services import WeatherService


def main() -> None:
    weather_service = WeatherService()
    # weather_service.service.how_is(location='shiraz')
    weather_service.interface.get(location='shiraz')


if __name__ == '__main__':
    main()
