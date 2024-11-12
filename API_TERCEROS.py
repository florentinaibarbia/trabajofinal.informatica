import requests

def obtener_datos_api_propia(endpoint):
    city = 'Roma'
    key = 'b9b664210634f1de44c25b915a76028f'
    # URL de tu API propia
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

    # Hacer la solicitud GET a tu API
    response = requests.get(url)
    
    if response.status_code == 200:  # Si la solicitud fue exitosa
        # Parsear los datos JSON
        data = response.json()

        # Extraer la información que necesitas
        fecha = data['fecha']
        city = data['ciudad']
        temp_max = data['temp_max']
        temp_min = data['temp_min']

        return fecha, city, temp_max, temp_min
    else:
        print("Error al obtener los datos de la API propia")
        return None
