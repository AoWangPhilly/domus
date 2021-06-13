import requests
import json
from os.path import join
import datetime as dt

# ------------------ OpenWeather API parameters -------------------------
with open(join('..', 'token.txt'), 'r') as token:
	TOKEN = token.read().replace('\n', '')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
CITY_NAME = 'Philadelphia'
UNITS = 'metric'

QUERY_URL = f'{BASE_URL}q={CITY_NAME}&appId={TOKEN}&units={UNITS}'
# ----------------------------------------------------------------------

class OpenWeatherMapReader:
	def __init__(self, query_url):
		self.query_url = query_url
	
	def get_temperature_and_humidity(self):
		response = requests.get(self.query_url)
		if response.status_code == 200:
			data = response.json()
			main = data['main']
			temp, temp_min, temp_max, humidity, time = main['temp'], main['temp_min'], main['temp_max'], main['humidity'], data['dt']
			time = dt.datetime.fromtimestamp(int(time)).isoformat()
			return time, humidity, temp, temp_min, temp_max


		
if __name__ == '__main__':
	weather_api = OpenWeatherMapReader(query_url=QUERY_URL) 
	print(weather_api.get_temperature_and_humidity())


