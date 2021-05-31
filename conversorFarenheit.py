gradosFarenheit = int(input("Introduce los grados Farenheit a convertir a Celsius: "))
# (32 °F − 32) × 5 / 9 = 0 °C
gradosCelsius = float(gradosFarenheit -32) * 5 / 9

print(str(gradosFarenheit) + " grados Farenheit son: " + str(round(gradosCelsius)) + " grados Celsius")