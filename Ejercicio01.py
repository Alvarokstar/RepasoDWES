numeros_v = []

for i in range(5):
    numero = int(input(f"Porfavor empiece a introducir los números, {i+1}: "))
    numeros_v.append(numero)

numeros_pares = []
for num in numeros_v:
    if num % 2 == 0:
        numeros_pares.append(num)

print("\nLista original por el usuario:", numeros_v)
print("Lista de números pares:", numeros_pares)
