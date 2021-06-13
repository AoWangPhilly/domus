import serial
import sqlite3
import datetime as dt

# Serial port: ls -l /dev/cu.usb*
SERIAL_PORT = '/dev/cu.usbmodem2201'

conn = sqlite3.connect('../sqlite/temperature_and_humidity.db')
cursor = conn.cursor()

ser = serial.Serial(SERIAL_PORT)
ser.flushInput()


while True:
	# Read line and decode to string
	ser_bytes = ser.readline().decode('utf-8')
		
	# Separate the string by \t and turn to floats
	# [humidity, temperature (in C)
	decoded_bytes = list(map(float, ser_bytes.split('\t')))
		
	time_read = dt.datetime.now().isoformat()
	humidity, temperature = decoded_bytes[0], decoded_bytes[1]
		
	cursor.execute('INSERT INTO room_metrics VALUES (?, ?, ?)', (time_read, humidity, temperature))
	conn.commit()

# Close out connection
conn.close() 
		
		


