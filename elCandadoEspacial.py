from colorama import Fore, Style
import time, random

titulo = "ESCAPE ROOM: EL CANDADO ESPACIAL"
print(titulo)
print(len(titulo)*"-")

print(
    Fore.YELLOW+"Dos hermanos, Alex y Elena, se encuentran en una sala mágica\n"
    "uno de los dos tiene que conseguir escapar y liberar al otro\n"
    "los dos se encuentran retenidos por unos escudos mágicos\n"
    "pero la clave para desactivar el escudo de uno de ellos esta oculta por algún lugar de la sala\n"
    "es hora de tomar decisiones, conseguir la clave e investigar los primeros pasos para iniciar la aventura\n"
    "en ocaciones habra que trabajar en equipo para resolver los enigmas\n"+Style.RESET_ALL
)
jugador = input(
    "Elige tu jugador\n"
    "A - Alex\n"
    "E - Elena\n"
)

if jugador == "A":
    print(
        "Has elegido a Alex, muy bien, eres un hacker de 14 años\n"
        "en forma, con gran agilidad fisica y mental y una gran capacidad de observación\n"
        "te desenvuelves bien en acertijos\n"
    )

    intro_password = input("Introduce la contraseña para romper el escudo mágico\n")

    if intro_password == "ABRACADABRA":
        time.sleep(5)
        print(
            "Se abre el escudo mágico de Alex!!, bien gracias a la contraseña que me dió Elena he podido liberarme\n"
            "Ahora debo encontrar la forma de liberar a Elena y salir de aqui\n"
        )
        numero_random = random.randint(1, 10) 
        time.sleep(3)
        print("Investigo por la sala y veo una puerta con un código numérico {} \n".format(numero_random))
        time.sleep(3)
        codigo = int(input("Introduce el código de la puerta\n"))
        time.sleep(3)
        codigo_final = int(input(
            "El código para abrir la puerta es la multiplicación de los dos códigos anteriores\n"
            "Introduce el código para abrir la puerta\n"
        ))
        time.sleep(3)

        if codigo_final == codigo * numero_random :
            print("Has conseguido abrir la puerta\n")
            teclado_magico = input(
                "Ves en el suelo un teclado mágico\n"
                "A - lo coges\n"
                "B - no lo coges\n"
            )

            if teclado_magico == "A":
                print("Pulsas el teclado y aparece un código: 857\n")
            elif teclado_magico == "B":
                print("Has decidido no coger el teclado, necesitas encontrar algo para continuar ...\n")
            else:
                print("No has seleccionado una opcion correcta\n")
        else: 
            print("La puerta permanece cerrada\n")

    else:
        print("El código es incorrecto\n")

if jugador == "E":
    print(
        "Has elegido a Elena, muy bien, eres una maga 5 años\n"
        "descifras contraseñas que nadie más sabe, tienes una gran inteligencia\n"
        "te desenvuelves bien en puzzles\n"
    )

    time.sleep(3)
    print("Se escucha un sonido y de repente pum aparece: \n")

    time.sleep(3)
    print("SUPERPAPI!!!!, Acuerdate pequeña tienes que trabajar con tu hermano la contraseña es: ABRACADABRA \n")

    time.sleep(3)
    print("Se escucha otro sonido y desaparece SUPERPAPI!!!\n")
    time.sleep(3)
    codigo_elena = int(input("Introduce el código para liberarme del escudo mágico\n"))

    if codigo_elena == 857:
        print("Habeis conseguido liberaros del candado espacial y salir con éxito de la ESCAPE ROOM, FELICIDADES!!!!\n")
    else:
        print("Necesitas el código correcto para liberarte\n")
