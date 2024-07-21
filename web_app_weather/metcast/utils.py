import requests
import datetime
from pathlib import Path
from dotenv import load_dotenv
import os


def get_weather_forecast(city):
    '''Функция, для получения данных о погоде по API.'''
    base_dir = Path(__file__).resolve().parent.parent
    env_file = base_dir.parent / '.env'

    if env_file.exists():
        load_dotenv(dotenv_path=env_file)

    api_key = os.getenv('api_key')
    date = datetime.date.today()
    url = (f'https://api.openweathermap.org/data/2.5/forecast?q={city}'
           f'&units=metric&lang=ru&date={date}&appid={api_key}')

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        forecast_data = response.json()

        for forecast in forecast_data['list'][:1]:
            dt_txt = forecast['dt_txt']
            temp = forecast['main']['temp']
            feels_like = forecast['main']['feels_like']
            weather_description = forecast['weather'][0]['description']
            return (f"{dt_txt}: Температура "
                    f"{temp}°C, Ощущается как "
                    f"{feels_like}°C, "
                    f"{weather_description}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
