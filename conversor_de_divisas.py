dolar_euro = 0.91
libra_euro = 1.16

opcion = input(
    "¿Qué conversión desea realizar?\n"
    "A - EUR/USD\n"
    "B - USD/EUR\n"
    "C - LIB/EUR\n"
    "D - EUR/LIB\n"
)


if opcion == "A":
    cantidad_euro = float(input("Introduce la cantidad de Euros a convertir: "))
    res_euro_dolar = round(cantidad_euro / dolar_euro, 2)
    print("La cantidad de {} Euros son {} Dólares al cambio".format(cantidad_euro, res_euro_dolar)) 
elif opcion == "B":
    cantidad_usd = float(input("Introduce la cantidad de Dólares a convertir: "))
    res_dolar_euro = round(cantidad_usd * dolar_euro, 2)
    print("La cantidad de {} Dólares son {} Euros al cambio".format(cantidad_usd, res_dolar_euro)) 
elif opcion == "C":
    cantidad_lib = float(input("Introduce la cantidad de Libras a convertir: "))
    res_libra_euro = round(cantidad_lib / libra_euro, 2)
    print("La cantidad de {} Libras son {} Euros al cambio".format(cantidad_lib, res_libra_euro))
elif opcion == "D":
    cantidad_eur = float(input("Introduce la cantidad de Euros a convertir: "))
    res_libra_euro = round(cantidad_eur * libra_euro, 2)
    print("La cantidad de {} Euros son {} Libras al cambio".format(cantidad_eur, res_libra_euro))
else:
    print("NOs has elegido una opción correcta")