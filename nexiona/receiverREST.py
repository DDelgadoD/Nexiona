import requests
import threading
import time
from nexiona.config import DATA

# CLASE QUE PERMITE HACER LAS LLAMADAS A API REST EN DIFERENTES HILOS DE EJECUCIÓN
# PARA GESTIONAR LA COLA CONCURRENTEMENTE YA QUE LOS MENSAJES LLEGARÁN DE UNO EN 
# UNO (PARA ELLO HE INDICADO EN API_DATA QUE EL LIMITE DE MENSAJES SEA 1)
class threaded_REST():

    def __init__(self, api_url, api_data, user, passwd):
        threading.Thread.__init__(self)
        self.url = api_url
        self.user = user
        self.passwd = passwd
        self.data = api_data

    def run(self):
        print("Starting to consume from API REST")
        threading.Thread(target=self.consume).setDaemon(True)

    def consume(self):
        while (True):
            try:
                r = requests.post(self.url, auth=(
                self.user, self.passwd), json=self.data)
            except requests.exceptions.RequestException as err:
                print(err)
                
            if r.json():
                DATA.append(r.json()[0]["payload"])
                print("New data Income from API REST")
            time.sleep(5)
