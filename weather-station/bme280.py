import bme280
import smbus2

class Bme280Sensor:
  def __init__(self, port=1, address=0x76):
    self.port = port
    self.address = address
    self.bus = smbus2.SMBus(self.port)

    bme280.load_calibration_params(self.bus, self.address)

  def get_all(self):
        bme280_data = bme280.sample(self.bus, self.address)
        humidity  = bme280_data.humidity
        pressure  = bme280_data.pressure
        temperature = bme280_data.temperature
        return temperature, humidity, pressure