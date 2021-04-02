# from .database import database
import logging

class WeatherService:
  def __init__(self):
  # self.db = database.WeatherDatabase()
    pass

  def archive_weather(self, weather_data: dict):
  # self.db.archive(weather_data['air_temperature'], weather_data['air_humidity'], weather_data['air_pressure'],
  #  weather_data['wind_speed'], weather_data['max_wind_gust'], weather_data['wind_direction'], weather_data['rainfall'])
    print(weather_data)

  def update_weather(self, weather_data: dict):
    


service = WeatherService()

