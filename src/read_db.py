import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('../sqlite/temperature_and_humidity.db')

cursor = conn.cursor()

# Query database
cursor.execute('SELECT rowid, * FROM room_metrics')
print(tabulate(cursor.fetchall(), tablefmt='pql'))

