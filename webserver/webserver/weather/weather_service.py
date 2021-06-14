from .database import database
import json
import decimal
import datetime

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%d/%m/%Y %H:%M:%S")

class WeatherService:
  def __init__(self):
    self.db = database.WeatherDatabase()

  def archive_weather(self, weather_data: dict):
    self.db.archive(weather_data['AIR_TEMPERATURE'], weather_data['AIR_HUMIDITY'], weather_data['AIR_PRESSURE'],
     weather_data['WIND_SPEED'], weather_data['MAX_WIND_GUST'], weather_data['WIND_DIRECTION'], weather_data['RAINFALL'], weather_data['CREATED'])

  def update_weather(self, weather_data: dict):
    self.db.update(weather_data['AIR_TEMPERATURE'], weather_data['AIR_HUMIDITY'], weather_data['AIR_PRESSURE'],
     weather_data['WIND_SPEED'], weather_data['MAX_WIND_GUST'], weather_data['WIND_DIRECTION'], weather_data['RAINFALL'], weather_data['UPDATED'])

  def get_current_weather(self):
    data = self.db.query('SELECT * FROM CURRENT_WEATHER')
    return json.dumps(data, cls=Encoder)

service = WeatherService()

