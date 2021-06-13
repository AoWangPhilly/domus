import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('../sqlite/temperature_and_humidity.db')

cursor = conn.cursor()

# Query database
cursor.execute('SELECT rowid, * FROM room_metrics')

column_names = list(map(lambda x: x[0], cursor.description))

print(tabulate(cursor.fetchall(), headers=column_names, tablefmt='pretty'))

cursor.execute('SELECT rowid, * FROM openweather')
column_names = list(map(lambda x: x[0], cursor.description))
print(tabulate(cursor.fetchall(), headers=column_names, tablefmt='pretty'))
