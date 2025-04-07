nombres = []
edades = []

for i in range (5):
    nombre = str(input(f"Introduzca los nombres de las personas {i+1}: "))
    edad = int(input(f"Introduzca las edades: {i+1}: "))

    nombres.append(nombre)
    edades.append(edad)

