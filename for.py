# Escribe un programa que almacene las asignaturas: Matemáticas, Física, Química e Historia en una lista y muestre por pantalla el mensaje 'Yo estudio <asignatura>' donde <asignatura> es cada una de las asignaturas de la lista

asignaturas = ["Matemáticas", "Física", "Química", "Historia"]

for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")

# Escribe un programa que pregunte por los productos de una cesta, separados por comas y muestre por pantalla cada uno de los productos en una línea distinta. (strip() elimina los espacios extra de al principio y al final del elemento)

productos = input("Ingresa el nombre de los productos de la cesta separados por comas: ")
cesta = productos.split(",")

cesta = [producto.strip() for producto in cesta]
print("\n".join(cesta))

# Escribe un programa que sume los puntos de 14 estudiantes y lo muestre por consola. Luego hacer otro programa que nos de la puntuación más alta

puntos = [150, 142, 185, 120, 171, 149, 24, 59, 68, 199, 78, 65, 89, 86]

suma = 0
for puntuacion in puntos:
    suma += puntuacion

print(f"suma total: {suma}") 

maxima_puntuacion = 0
for puntuacion in puntos:
    if puntuacion > maxima_puntuacion:
        maxima_puntuacion = puntuacion

print(f"Valor más alto: {maxima_puntuacion}")

# Crea un programa que sume los números del 1 al 100

suma = 0
for numero in range(1, 101):
    suma += numero

print(suma)

# Crea un programa que muestre los números del 1 al 100 cuando el número es divisible por 3 debería imprimir "Fizz", cuando el número es divisible por 5 debería imprimir "Buzz" pero cuando el número es divisible por 3 y 5 ejemplo 15 debería imprimir "FizzBuzz"

for numero in range(1, 101):

    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)