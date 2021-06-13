import sqlite3
from openweathermap_reader import OpenWeatherMapReader, QUERY_URL
from serial_reader import SerialReader, SERIAL_PORT 

conn = sqlite3.connect('../sqlite/temperature_and_humidity.db')
cursor = conn.cursor()

ser_reader = SerialReader(port=SERIAL_PORT)
openweather_reader = OpenWeatherMapReader(query_url=QUERY_URL)

while True:
	try:
		cursor.execute('INSERT INTO room_metrics VALUES (?, ?, ?)', ser_reader.read_serial())
		conn.commit()

		cursor.execute('INSERT INTO openweather VALUES (?, ?, ?, ?, ?)', openweather_reader.get_temperature_and_humidity())
		conn.commit()

	except Exception as e:
		print(e)
		break

conn.close()
