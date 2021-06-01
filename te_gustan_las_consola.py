titulo = "Bienvenido al ejercicio 2 ¿Cuánto te gustan las consolas?"
print(titulo)
print(len(titulo)*"-")

puntuacion = 0

pregunta1 = input(
    "¿Conoces la Game Gear?\n"
    "A - Sí la conozco\n"
    "B - No la conozco\n"
    "C - Tengo una\n"
)

if (pregunta1 == "A"):
    puntuacion += 5
elif(pregunta1 == "B"):
    puntuacion += 0
elif(pregunta1 == "C"):
    puntuacion += 10
else:
    puntuacion += 0
    print("Has introducido una respuesta errónea")

pregunta2 = input(
    "¿Conoces la Megadrive?\n"
    "A - Sí la conozco\n"
    "B - No la conozco\n"
    "C - Tengo una\n"
)

if (pregunta2 == "A"):
    puntuacion += 5
elif(pregunta2 == "B"):
    puntuacion += 0
elif(pregunta2 == "C"):
    puntuacion += 10
else:
    puntuacion += 0
    print("Has introducido una respuesta errónea")

pregunta3 = input(
    "¿Conoces la Super Nintendo?\n"
    "A - Sí la conozco\n"
    "B - No la conozco\n"
    "C - Tengo una\n"
)

if (pregunta3 == "A"):
    puntuacion += 5
elif(pregunta3 == "B"):
    puntuacion += 0
elif(pregunta3 == "C"):
    puntuacion += 10
else:
    puntuacion += 0
    print("Has introducido una respuesta errónea")

print("Su puntuación actual es: {} ".format(puntuacion))