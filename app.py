from flask import Flask, jsonify, request
from db.db_manager import save_clint_europe_cities
from db.db_manager import load_client_europe_cities
from db.europe_cities import 

app = Flask(__name__)
client_cities = load_client_europe_cities()

@app.route('/hello', methods=['GET'])
def hello():
    return "hello"

@app.route("/api/prometheus/europe_cities", methods=['GET'])
def get_client_europe_cities():
    city_cl = load_client_europe_cities()
    return jsonify([c.serialize() for c in city_cl])

@app.route('/api/prometheus/europe_cities', methods=['POST'])
def create_client_europe_cities():
    client_req_json = request.json
    save_clint_europe_cities(client_req_json)
    return jsonify(client_req_json)

@app.route("/api/prometheus/europe_cities/reports", methods=['GET'])
def get_city_by_date():
    date = request.args.get('date')
    if date is None:
        return jsonify({"error": "no date info given"})
    else:
        # Filtrar las ciudades por la fecha especificada
        filtered_cities = [city for city in client_cities if city.date == date]

        # Calcular el promedio del clima de las ciudades filtradas
        average_weather = sum(int(city.weather) for city in filtered_cities) / len(filtered_cities)
        return jsonify({"average_weather": average_weather})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
