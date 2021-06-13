clean: 
	rm sqlite/temperature_and_humidity.db

run:
	cd src && python create_db.py && python read_to_sqlite.py

