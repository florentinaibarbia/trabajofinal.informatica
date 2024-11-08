import requests

def obtener_datos_api_propia(endpoint):
    # URL de tu API propia
    url = f'http://tuservidorapi.com/{endpoint}'

    # Hacer la solicitud GET a tu API
    response = requests.get(url)
    
    if response.status_code == 200:  # Si la solicitud fue exitosa
        # Parsear los datos JSON
        data = response.json()

        # Extraer la información que necesitas
        fecha = data['fecha']
        ciudad = data['ciudad']
        temp_maxima = data['temp_maxima']
        temp_minima = data['temp_minima']

        return fecha, ciudad, temp_maxima, temp_minima
    else:
        print("Error al obtener los datos de la API propia")
        return None
