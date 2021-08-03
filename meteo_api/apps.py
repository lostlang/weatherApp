from django.apps import AppConfig
from os import environ

from requests import Session


class MeteoApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'meteo_api'


class MeteoApi:
    token = environ.get("metio_token")
    call = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=ru'
    default_city = 'Moscow'
    session = Session()
    need_data = [['weather', 'description', "weather"],
                 ['main', 'temp', "degree"],
                 ['wind', 'speed', "wind_speed"]]

    def get_url(self):
        return self.call.format(self.default_city, self.token)

    def get_data(self):
        callback = self.session.get(self.get_url()).json()
        out_data = dict()
        for data in self.need_data:
            callback_for_key1 = callback[data[0]]
            if len(callback_for_key1) == 1:
                callback_for_key1 = callback_for_key1[0]
            callback_for_key2 = callback_for_key1[data[1]]
            out_data[data[2]] = callback_for_key2
        return out_data
