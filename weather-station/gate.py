import requests

class Gate:
  def __init__(self):
    self.url='http://localhost:5000'


  def save_current_weather(self, json: dict):
    print("current: "+json)
    requests.POST(self.url + '/current', data=json)

  def archive_weather(self, json: dict):
    print("archive: "+json)
    requests.POST(self.url + '/archive', data=json)