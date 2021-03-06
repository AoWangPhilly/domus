import serial
import datetime as dt
from typing import List

# Serial port: ls -l /dev/cu.usb*
SERIAL_PORT = '/dev/cu.usbmodem2201'

class SerialReader:
	def __init__(self, port: str):
		self.ser = serial.Serial(port)
		self.ser.flushInput()
		
	def read_serial(self) -> List[str]:
		# Read line and decode to string
		ser_bytes = self.ser.readline().decode('utf-8')
		return self.__clean_serial_output(ser_bytes)
	
	def __clean_serial_output(self, output: str) -> List[str]:
		# Separate the string by tab and turn into floats
		# [humidity, temperature (C)]
		decoded_bytes = list(map(float, output.split('\t')))
		
		# Include time when read
		date = dt.datetime.now().isoformat()
		return [date] + decoded_bytes
		
if __name__ == '__main__':
	serial_port = SerialReader(SERIAL_PORT)
	print(serial_port.read_serial())
