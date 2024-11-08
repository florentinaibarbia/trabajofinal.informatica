from flask import Flask, jsonify, request
from db.db_manager import save_client_statistics
from db.db_manager import load_client_statistics
import statistics

app = Flask(__name__)
client_stats = load_client_statistics()

#Este endpoint (/hello) verifica que el servidor esté activo.
@app.route('/hello', methods=['GET'])
def hello():
    return "Welcome to The Weather API!"


#Este endpoint devuelve todos los registros de clima en formato JSON.
@app.route("/api/weather/statistics", methods=['GET'])
def get_all_weather_statistics():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM weather")
    records = cursor.fetchall()
   
    weather_data = [{"id": r[0], "date": r[1], "city": r[2], "max_temp": r[3], "min_temp": r[4]} for r in records]
    return jsonify(weather_data)

#Este endpoint permite agregar un nuevo registro de clima.
@app.route('/api/weather/statistics', methods=['POST'])
def create_weather_statistics():
    new_data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO weather (date, city, max_temp, min_temp)
        VALUES (?, ?, ?, ?)
    """, (new_data['date'], new_data['city'], new_data['max_temp'], new_data['min_temp']))
    db.commit()
    return jsonify({"message": "Weather data added successfully"}), 201

#Proporciona las estadísticas promedio de temperatura para una fecha específica.
@app.route("/api/weather/statistics/reports/<date>", methods=['GET'])
def get_weather_stat_by_date(date):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT max_temp, min_temp FROM weather WHERE date = ?", (date,))
    records = cursor.fetchall()

    if not records:
        return jsonify({"error": "No data available for the given date"}), 404

    max_temps = [r[0] for r in records]
    min_temps = [r[1] for r in records]
    average_max_temp = statistics.mean(max_temps)
    average_min_temp = statistics.mean(min_temps)
    
    return jsonify({
        "date": date,
        "average_max_temp": average_max_temp,
        "average_min_temp": average_min_temp
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
