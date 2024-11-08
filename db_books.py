import sqlite3

DATABASE_NAME = "clima.db"  # Nombre de la base de datos

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    # Crear la tabla 'clima' con las columnas
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS clima (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Columna id para identificación única
        fecha TEXT NOT NULL,                   -- Fecha del registro
        ciudad TEXT NOT NULL,                  -- Ciudad a la que corresponde el clima
        temp_maxima REAL NOT NULL,             -- Temperatura máxima
        temp_minima REAL NOT NULL              -- Temperatura mínima
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
