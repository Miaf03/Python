# Crea un programa que pida dos números y realice su suma, resta, multiplicación y división. Compruebe cuál número es mayor o si los dos son iguales, Si la suma de ambos es mayor a 100 muestra “La suma es alta”, si no “La suma es baja”.

uno = int(input("Ingresa un número: "))
dos = int(input("Ingresa otro número: "))

print(f"La suma de {uno} + {dos} es igual a: {uno + dos}")
print(f"La resta de {uno} - {dos} es igual a: {uno - dos}")
print(f"La multiplicacíon de {uno} * {dos} es igual a: {uno * dos}")
print(f"La división de {uno} / {dos} es igual a: {uno / dos:.2f}")

if uno > dos:
    print(f"El número {uno} es mayor a {dos}")
elif uno < dos:
    print(f"El número {dos} es mayor que {uno} ")
else:
    print("Ambos valores son iguales")
    
if uno + dos > 100:
    print("La suma es alta")
else:
    print("La suma es baja")


# Crea una lista con 5 nombres y usa un bucle for para imprimir cada uno. Agrega un nombre más a la lista y vuelve a imprimirla. Usa un condicional dentro del bucle para imprimir solo los nombres que tengan más de 5 letras.

lista = ["Memo", "Lalo", "Mia", "Lulu", "Miguel"]

print("\nLista de nombres:\n")
for nombre in lista:
    print(nombre)

lista.append("Andrea")

print("\nLista de nombres actualizada:\n")
for nombre in lista:
    print(nombre)
    
print("\nNombres con más de 5 letras:\n")
for nombre in lista:
    if len(nombre) > 5:
        print(nombre)