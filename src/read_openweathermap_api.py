import requests
import json
from os.path import join

with open(join('..', 'token.txt'), 'r') as token:
	API_TOKEN = token.read().replace('\n', '')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
CITY_NAME = 'Philadelphia'
UNITS = 'metric'

URL_QUERY = f'{BASE_URL}q={CITY_NAME}&appId={API_TOKEN}&units={UNITS}'

print(URL_QUERY)
response = requests.get(URL_QUERY)
print(response.json())




