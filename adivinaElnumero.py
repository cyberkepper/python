import random

print("Trata de adivinar mi numero:")
print("----------------------------")
numeroGanador = random.randint(1, 10)
adivinaElnumero = int(input("[*] Introduce un numero del 1 al 10: "))
if adivinaElnumero > 10:
    print("El numero introducido es demasiado grande")
    exit(0)
if adivinaElnumero < 1:
    print("El numero introducido es demasiado pequeño")
    exit(0)
if adivinaElnumero != numeroGanador:
    print("El numero no es correcto")
if adivinaElnumero == numeroGanador:
    print("Felicidades acertaste el numero")