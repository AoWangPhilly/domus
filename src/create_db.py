import sqlite3

# Connect to database
conn = sqlite3.connect('../sqlite/temperature_and_humidity.db')

# Create a cursor
cursor = conn.cursor()

# Create table
cursor.execute(
'''CREATE TABLE room_metrics (
	date TEXT,
	humidity REAL,
	temperature REAL
 )''')

cursor.execute(
'''CREATE TABLE openweather (
	date TEXT,
	humidity REAL,
	temperature REAL,
	temperature_min REAL,
	temperature_max REAL,
	UNIQUE (date) ON CONFLICT IGNORE			
)''')

conn.close()
