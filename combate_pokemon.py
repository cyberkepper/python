from random import randint

titulo = "Bienvenidos a Combate Pokémon"
print(len(titulo)*"=")
print(titulo)
print(len(titulo)*"=")

vida_inicial_pikachu = 80
vida_actual_pikachu = 80

vida_inicial_squirtle = 90
vida_actual_squirtle = 90

while vida_actual_pikachu > 0 or vida_actual_squirtle > 0:
    
    # Turno de Pikachu
    print("Turno Pikachu\n")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola voltio")
        vida_actual_squirtle -= 10
    else:
        print("Pikachu ataca con onda de trueno")
        vida_actual_squirtle -= 11

    # Turno de Squirtle
    print("Turno Squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
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

    print("La vida de Pikachu es: [{}] {}".format(int(round((vida_actual_pikachu * 10) / vida_inicial_pikachu, 10)) * "#", vida_actual_pikachu))
    print("la vida de Squirtle es: [{}] {}".format(int(round((vida_actual_squirtle * 10) / vida_inicial_squirtle, 10)) * "#", vida_actual_squirtle))

if vida_actual_pikachu > vida_actual_squirtle:
    print("Pikachu Wins!!")
else:
    print("Squirtle Wins!!")    