import MySQLdb, datetime, http.client, json, os
import io
import gzip
import time

class MysqlDatabase:
    def __init__(self):
        credentials_file = os.path.join(os.path.dirname(__file__), "credentials.mysql")
        f = open(credentials_file, "r")
        credentials = json.load(f)
        f.close()
        for key, value in credentials.items(): #remove whitespace
            credentials[key] = value.strip()

        self.connection = MySQLdb.connect(user=credentials["USERNAME"], password=credentials["PASSWORD"], database=credentials["DATABASE"])
        self.cursor = self.connection.cursor()

    def execute(self, query, params = []):
      cursor = self.connection.cursor()
      try:
          cursor.execute(query, params)
          self.connection.commit()
      except:
          self.connection.rollback()
          raise
      cursor.close()
        

    def query(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def __del__(self):
        self.connection.close()

class WeatherDatabase:
    def __init__(self):
        self.db = MysqlDatabase()
        self.archive_template = "INSERT INTO WEATHER_ARCHIVE (AIR_TEMPERATURE, AIR_HUMIDITY, AIR_PRESSURE, WIND_SPEED, MAX_WIND_GUST, WIND_DIRECTION, RAINFALL, CREATED) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
        self.update_template = "REPLACE INTO CURRENT_WEATHER (ID, AIR_TEMPERATURE, AIR_HUMIDITY, AIR_PRESSURE, WIND_SPEED, MAX_WIND_GUST, WIND_DIRECTION, RAINFALL, UPDATED) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"


    def archive(self, air_temperature, air_humidity, air_pressure, wind_speed, max_wind_gust, wind_direction, rainfall, created):
        params = (
            air_temperature,
            air_humidity,
            air_pressure,
            wind_speed,
            max_wind_gust,
            wind_direction,
            rainfall,
            created )
        print(self.archive_template % params)
        self.db.execute(self.archive_template, params)

    def update(self, air_temperature, air_humidity, air_pressure, wind_speed, max_wind_gust, wind_direction, rainfall, updated):
        params = (1,
            air_temperature,
            air_humidity,
            air_pressure,
            wind_speed,
            max_wind_gust,
            wind_direction,
            rainfall,
            updated )
        print(self.update_template % params)
        self.db.execute(self.update_template, params)

    def query(self, query):
      return self.db.query(query)