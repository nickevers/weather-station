import requests
import json
import datetime

class Gate:
  def __init__(self):
    self.url='http://localhost:5000'


  def save_current_weather(self, data: dict):
    data.update({'UPDATED': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    print("current: "+json.dumps(data))
    requests.post(self.url + '/current', json=data)

  def archive_weather(self, data: dict):
    data.update({'CREATED': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    print("archive: "+json.dumps(data))
    requests.post(self.url + '/archive', json=data)