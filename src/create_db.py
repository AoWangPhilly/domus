import sqlite3

# Connect to database
conn = sqlite3.connect('../sqlite/temperature_and_humidity.db')

# Create a cursor
cursor = conn.cursor()

# Create table
cursor.execute(
'''CREATE TABLE room_metrics (
	date text,
	humidity text,
	temperature text
 )''')
