# Importamos la librería 'requests', que nos permite hacer peticiones HTTP 
# (consultar páginas web o APIs desde Python).
import requests

# Guardamos la dirección URL de la API que nos servirá los chistes.
url = "https://icanhazdadjoke.com/"

# Definimos los encabezados (headers) de la petición.
# Con 'Accept': 'application/json' le pedimos al servidor que nos devuelva 
# los datos en formato JSON estructurado en lugar de una página HTML completa.
headers = {"Accept": "application/json"}

# Iniciamos un bucle infinito para seguir pidiendo chistes hasta que el usuario decida salir.
while True:
    # Hacemos una petición HTTP GET a la API enviando la URL y los encabezados.
    respuesta = requests.get(url, headers=headers)
    
    # Convertimos la respuesta recibida (que viene en texto JSON) a un diccionario de Python.
    datos = respuesta.json()
    
    # Extraemos y mostramos únicamente el texto del chiste usando la clave "joke".
    print(datos["joke"])

    # Solicitamos una acción al usuario a través de la consola.
    otra = input("Enter para otro chiste, q para salir: ")
    
    # Si el usuario escribe 'q' (o 'Q' si se presiona la tecla), rompemos el bucle y termina el programa.
    if otra == "q":
        break