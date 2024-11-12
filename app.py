from flask import Flask, jsonify, request
from db_manager import save_europe_cities
from db_manager import load_europe_cities
import europe_cities

app = Flask(__name__)
client_stats = load_europe_cities()

#Este endpoint (/hello) verifica que el servidor esté activo.
@app.route('/hello', methods=['GET'])
def hello():
    return "Welcome to The Weather API!"


#Este endpoint devuelve todos los registros de clima en formato JSON.
@app.route("/api/weather/europe_cities", methods=['GET'])
def get_all_europe_cities():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM weather")
    records = cursor.fetchall()
   
    weather_data = [{"id": r[0], "date": r[1], "city": r[2], "temp_max": r[3], "temp_min": r[4]} for r in records]
    return jsonify(weather_data)

#Este endpoint permite agregar un nuevo registro de clima.
@app.route('/api/weather/europe_cities', methods=['POST'])
def create_europe_cities():
    new_data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO weather (date, city, max_temp, min_temp)
        VALUES (?, ?, ?, ?)
    """, (new_data['date'], new_data['city'], new_data['temp_max'], new_data['temp_min']))
    db.commit()
    return jsonify({"message": "Weather data added successfully"}), 201

#Proporciona las estadísticas promedio de temperatura para una fecha específica.
@app.route("/api/weather/europe_cities/reports/<date>", methods=['GET'])
def get_weather_stat_by_date(date):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT max_temp, min_temp FROM weather WHERE date = ?", (date,))
    records = cursor.fetchall()

    if not records:
        return jsonify({"error": "No data available for the given date"}), 404

    temp_max = [r[0] for r in records]
    temp_min = [r[1] for r in records]
    average_max_temp = europe_cities.mean(temp_max)
    average_min_temp = europe_cities.mean(temp_min)
    
    return jsonify({
        "date": date,
        "average_max_temp": average_max_temp,
        "average_min_temp": average_min_temp
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
