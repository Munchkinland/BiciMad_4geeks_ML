# URL de la API del ayuntamiento
api_url = "https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"

# Parámetros de la solicitud (reemplaza con tus propios valores)
headers = {
    'email': 'ruben.c_ac@icloud.com',
    'password': 'Prada2024!',
    #'X-ApiKey': 'tu_api_key',
    #'X-ClientId': 'tu_cliente_id',
    #'passKey': 'tu_pass_key'
}

# Realizar la solicitud a la API
import requests
response = requests.get(api_url, headers=headers)

# Verificar la respuesta
if response.status_code == 200:
    # La solicitud fue exitosa, puedes procesar la respuesta JSON
    data = response.json()
    print(data)
else:
    # La solicitud no fue exitosa, muestra el código de estado y el contenido de la respuesta
    print(f"Error: {response.status_code}")
    print(response.text)