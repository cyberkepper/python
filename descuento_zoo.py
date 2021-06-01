
edad = int(input("Digame su edad: "))

tipoDeCarnet = input("Digame su tipo de carnet (E para Estudiante / P para Pensionista / F Familia numerosa / N Nada): ")

if (25 <= edad <= 35 and tipoDeCarnet == "E") or edad < 10 or (edad >= 65 and tipoDeCarnet == "P") or (tipoDeCarnet == "F"):
    print("Se te aplica el descuento")
else:
    print("No se te aplica el descuento")