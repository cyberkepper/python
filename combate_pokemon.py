from random import randint
import os

titulo = "Bienvenidos a Combate Pokémon"
print(len(titulo)*"=")
print(titulo)
print(len(titulo)*"=")

TAMANO_BARRA_VIDA = 20

VIDA_INICIAL_PIKACHU = 80
vida_actual_pikachu = 80

VIDA_INICIAL_SQUIRTLE = 90
vida_actual_squirtle = 90

while vida_actual_pikachu > 0 or vida_actual_squirtle > 0:
    
    # Turno de Pikachu
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

    print("Turno Pikachu\n")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola voltio")
        vida_actual_squirtle -= 10
    else:
        print("Pikachu ataca con onda de trueno")
        vida_actual_squirtle -= 11

    print("La vida de Pikachu es: [{}] [{}/{}]".format(int(round((vida_actual_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU, 10)) * "#", vida_actual_pikachu, VIDA_INICIAL_PIKACHU))
    print("la vida de Squirtle es: [{}] [{}/{}]".format(int(round((vida_actual_squirtle * TAMANO_BARRA_VIDA) / VIDA_INICIAL_SQUIRTLE, 10)) * "#", vida_actual_squirtle, VIDA_INICIAL_SQUIRTLE))

    if vida_actual_squirtle < 0:
        print("Pikachu Wins!!")
        vida_actual_squirtle = 0 
        exit()
    if vida_actual_pikachu < 0:
        print("Squirtle Wins!!")
        vida_actual_pikachu = 0 
        exit()
    print("\n---------------\n")

    # Turno de Squirtle
    print("Turno Squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con placaje")
        vida_actual_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con pistola de agua")
        vida_actual_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con burbuja")
        vida_actual_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle hace nada ...")

    print("La vida de Pikachu es: [{}] {}".format(int(round((vida_actual_pikachu * TAMANO_BARRA_VIDA) / VIDA_INICIAL_PIKACHU, 10)) * "#", vida_actual_pikachu))
    print("la vida de Squirtle es: [{}] {}".format(int(round((vida_actual_squirtle * TAMANO_BARRA_VIDA) / VIDA_INICIAL_SQUIRTLE, 10)) * "#", vida_actual_squirtle))

    print("Pulsa ENTER para continuar ...\n")

