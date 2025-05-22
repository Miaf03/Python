# Escribe un programa que almacene los cursos: Matemáticas, Física, Química e Historia en una lista y los muestre por pantalla

cursos = ["Matemáticas", "Física", "Química", "Historia"]
print(cursos)

# Suma todos los números de la lista [1, 2, 3, 4, 5] y muestra el resultado

lista = [1, 2, 3, 4, 5]
suma = sum(lista)

print(f"La suma de {lista} es: {suma}")

# Dada la lista [4, 7, 2, 9, 5], encuentra el número máximo

lista = [4, 7, 2, 9, 5]
maximo = max(lista)

print(f"El número máximo de {lista} es: {maximo}")

# Genera una lista con los números del 1 al 10 usando un bucle for

numeros = []

for num in range(1, 11):
    numeros.append(num)
    
print(f"Lista de números del 1 al 10: {numeros}")

# Crea una nueva lista que contenga el cuadrado de cada número en la lista [1, 2, 3, 4, 5]

lista = [1, 2, 3, 4, 5]
cuadrado = []

for numero in lista:
    cuadrado.append(numero ** 2)

print(f"Lista: {lista}")
print(f"Cuadrado: {cuadrado}")

# Cuenta la cantidad de elementos de la lista [10, 20, 30, 40, 50] sin usar la función len()

lista = [10, 20, 30, 40, 50]
contador = 0

for elemento in lista:
    contador += 1

print(f"La cantidad de elementos en la lista es: {contador}")

# Crea una lista de números y usa un bucle para imprimir solo los números mayores a 10.

lista = [2, 4, 38, 19, 36, 2, 37]
mayor_a_10 = []

for numero in lista:
    if numero > 10:
        mayor_a_10.append(numero)
    
print(mayor_a_10)