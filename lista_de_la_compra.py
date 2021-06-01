import os
# Limpiar pantalla
if os.name == "posix":
    os.system ("clear")
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    os.system ("cls")

titulo = "Programa Carrito de la compra"
print(len(titulo)*"=")
print(titulo)
print(len(titulo)*"=")

carrito_de_la_compra = []
agregar = None

while agregar != ["Q"]: #while True: siempre se ejecutaría hasta poner un break, el pass continuaría

    articulo = input("¿Qué desea comprar? ")
    agregar = input("¿Seguro que desea agregar {} al carrito de la compra (S/N) [Q] para salir \n".format(articulo))

    if agregar == "S" or agregar == "s":
        if articulo not in carrito_de_la_compra:
            carrito_de_la_compra.append(articulo)
            print("{} añadido al carrito!".format(articulo))
        else:
            print("{} ya esta en el carrito!!".format(articulo))
    elif agregar == "N":
        print("{}, no se agrega al carrito!!".format(articulo))
    else:
        print("El carrito contiene: {}".format(carrito_de_la_compra))