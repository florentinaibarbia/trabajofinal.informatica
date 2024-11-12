import csv
import europe_cities
from product import Report
import sqlite3

def save_europe_cities(info):
    with open('europe_cities.csv', 'a') as client_europe_cities_file:
        header = ['date', 'city', 'weather_description', 'temp_max', 'temp_min','humidity']

        writer = csv.DictWriter(client_europe_cities_file, fieldnames=header)

        if client_europe_cities_file.tell() == 0:
            writer.writeheader()

        writer.writerow(info)


def load_europe_cities():
    client_europe_cities = []
    with open('europe_cities.csv', 'r') as europe_cities_file:
        rows = csv.DictReader(europe_cities_file)

        for row in rows:
            client_europe_cities.append(
                Report(
                    row['date'],
                    row['city'],
                    row['weather.description'],
                    row['temp_max']
                    row['temp_min']
                    row['humidity']
                )
            )
        return client_europe_cities

def europe_cities_average():
    client_europe_cities = load_europe_cities()
    average_weather = europe_cities.mean([report.temp_max and report.temp_min for report in client_europe_cities])
    return average_weather
'''

DATABASE_NAME = "weather.db"  # Nombre de la base de datos

def get_db():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def create_tables():
    # Crear la tabla 'clima' con las columnas
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS clima (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Columna id para identificación única
        date TEXT NOT NULL,                   -- Fecha del registro
        city TEXT NOT NULL,                  -- Ciudad a la que corresponde el clima
        temp_max REAL NOT NULL,             -- Temperatura máxima
        temp_min REAL NOT NULL              -- Temperatura mínima
        humidity REAL NOT NULL              -- Humedad
    );
    """

    # Conexión a la base de datos y ejecución del SQL
    db = get_db()
    cursor = db.cursor()
    cursor.execute(sql_create_table)  # Ejecutar la consulta SQL
    db.commit()  # Confirmamos los cambios
    db.close()   # Cerramos la conexión

# Llamada para crear las tablas
create_tables()
'''
