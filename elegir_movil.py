titulo = "Bienvenido al Super Elegidor de Movil 2.0"
print(titulo)
print(len(titulo) * "-")

tipo = input(
    "¿Que SO prefiere iOS o Android?\n"
    "A - Android\n"
    "B - iOS\n"
)

if tipo == "A":
    tienes_dinero = input(
        "¿Tienes dinero?\n"
        "S - sí\n"
        "N - no\n"
    )
    if tienes_dinero == "N":
        print("Comprate un movil Android Chino por 100€")
    elif tienes_dinero == "S":
        con_camara = input(
            "¿Te importa la cámara del movil?\n"
            "S - sí\n"
            "N - no\n"
        )
        if con_camara == "S":
            print("Comprate un Google Pixel con Supercamara")
        elif con_camara == "N":
            print("Comprate un Android calidad precio")
        else:
            print("Has elegido una opcion inválida")
    else:
        print("Has elegido una opcion inválida")

elif tipo == "B":
    tienes_dinero = input(
        "¿Tienes dinero?\n"
        "S - sí\n"
        "N - no\n"
    )
    if tienes_dinero == "N":
        print("Comprate un iPhone de segunda Mano")
    elif tienes_dinero == "S":
        con_camara = input(
            "¿Te importa la cámara del movil?\n"
            "S - sí\n"
            "N - no\n"
        )
        if con_camara == "S":
            print("Comprate un Iphone Ultra Pro Max del copon")
        elif con_camara == "N":
            print("Comprate un Iphone cutre salchichero con camara rota")
        else:
            print("Has elegido una opcion inválida")
    else:
        print("Has elegido una opcion inválida")

else:
    print("No ha elegido entre las dos opciones disponibles")