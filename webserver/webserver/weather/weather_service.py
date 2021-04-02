from .database import database

class WeatherService:
  def __init__(self):
    self.db = database.WeatherDatabase()

  def archive_weather(self, weather_data: dict):
    self.db.archive(weather_data['AIR_TEMPERATURE'], weather_data['AIR_HUMIDITY'], weather_data['AIR_PRESSURE'],
     weather_data['WIND_SPEED'], weather_data['MAX_WIND_GUST'], weather_data['WIND_DIRECTION'], weather_data['RAINFALL'])

  def update_weather(self, weather_data: dict):
    self.db.update(weather_data['AIR_TEMPERATURE'], weather_data['AIR_HUMIDITY'], weather_data['AIR_PRESSURE'],
     weather_data['WIND_SPEED'], weather_data['MAX_WIND_GUST'], weather_data['WIND_DIRECTION'], weather_data['RAINFALL'])


service = WeatherService()

