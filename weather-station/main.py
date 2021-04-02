from bme280 import Bme280Sensor
from time import sleep
from gate import Gate

def calc_avg(measurements: []) -> dict:
  total_temperature = 0
  total_humidity = 0
  total_pressure = 0
  total_wind_speed = 0
  max_wind_gust = 0
  wind_direction = 0
  total_rainfall = 0

  for measurement in measurements:
    total_temperature += measurement['AIR_TEMPERATURE']
    total_humidity += measurement['AIR_HUMIDITY']
    total_pressure += measurement['AIR_PRESSURE']
    total_wind_speed += measurement['WIND_SPEED']
    if measurement['MAX_WIND_GUST'] > max_wind_gust:
      max_wind_gust = measurement['MAX_WIND_GUST']
    wind_direction += measurement['WIND_DIRECTION']
    total_rainfall += measurement['RAINFALL']

  return {'AIR_TEMPERATURE': total_temperature/len(measurements), 'AIR_HUMIDITY': total_humidity/len(measurements), 
  'AIR_PRESSURE': total_pressure/len(measurements), 'WIND_SPEED': total_wind_speed/len(measurements),
  'MAX_WIND_GUST': max_wind_gust, 'WIND_DIRECTION': wind_direction/len(measurements),'RAINFALL': total_rainfall}



def main():
  archive = []
  bme280 = Bme280Sensor()
  gate = Gate()

  while True:
    current_weather = {}
    temperature, humidity, pressure = bme280.get_all()
    bme280_data = {'AIR_TEMPERATURE': temperature, 'AIR_HUMIDITY': humidity, 'AIR_PRESSURE': pressure}
    current_weather.update(bme280_data)
    # Mock other data
    mock_data = {'WIND_SPEED': 0, 'MAX_WIND_GUST': 0, 'WIND_DIRECTION': 0, 'RAINFALL': 0}
    current_weather.update(mock_data)
    archive.append(current_weather)
    gate.save_current_weather(current_weather)
    if (len(archive) >= 12):
      gate.archive_weather(calc_avg(archive))
      archive = []

    sleep(5)


if __name__ == "__main__":
    main()