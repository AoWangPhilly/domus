import sqlite3
from tabulate import tabulate

DB_PATH = '../sqlite/temperature_and_humidity.db'

def read_table(table_name: str, db_path: str=DB_PATH) -> None:
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    # Query database
    cursor.execute(f'SELECT rowid, * FROM {table_name}')

    column_names = list(map(lambda x: x[0], cursor.description))

    print(tabulate(cursor.fetchall(), headers=column_names, tablefmt='pretty'))


if __name__ == '__main__':
    read_table('room_metrics')
    read_table('openweather')

