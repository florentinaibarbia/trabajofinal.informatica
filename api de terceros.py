import requests
import json

def obtener_datos_meteorologicos(ciudad):
    # Tu API key de OpenWeather
    api_key = 'b9b664210634f1de44c25b915a76028f'
    
    # URL de la API (usamos el endpoint de clima actual)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
    
    # Hacer la solicitud GET
    response = requests.get(url)
    
    if response.status_code == 200:  # Si la solicitud fue exitosa
        # Parsear los datos JSON
        data = response.json()

        # Extraer los datos que necesitas
        temp_maxima = data['main']['temp_max']
        temp_minima = data['main']['temp_min']
        fecha = data['dt']  # Timestamp en segundos (puedes convertirlo a una fecha legible)

        return fecha, ciudad, temp_maxima, temp_minima
    else:
        print("Error al obtener los datos de la API")
        return None
