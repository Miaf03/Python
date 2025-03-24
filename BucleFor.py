
# Imprime los números del 1 al 10 usando un bucle for

for numero in range(1, 11):
    print(numero)
    
# Imprime los números pares del 1 al 20

for numero in range(2, 21, 2):
    print(numero)
    
# Pide al usuario que ingrese una palabra y cuenta cuántas vocales tiene

palabra = input("Ingresa una palabra: ")
contador = 0

for letra in palabra:
    
    if letra in "aeiouAEIOU":
        contador += 1
        
print(f"Hay {contador} vocales en '{palabra}'")

# Usa un bucle for para imprimir cada carácter de la cadena "Python" en una línea separada

cadena = "Python"

for letra in cadena:
    print(letra)

# Escribe un programa que almacene las asignaturas: Matemáticas, Física, Química e Historia en una lista y muestre por pantalla el mensaje 'Yo estudio <asignatura>' donde <asignatura> es cada una de las asignaturas de la lista

asignaturas = ["Matemáticas", "Física", "Química", "Historia"]

for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")

# Escribe un programa que pregunte por los productos de una cesta, separados por comas y muestre por pantalla cada uno de los productos en una línea distinta. "strip() elimina los espacios extra de al principio y al final del elemento"

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
        
# Pide al usuario un número (como cadena) y suma todos sus dígitos

cadena = input("Ingresa un número: ")
contador = 0

for digito in cadena:
    contador += int(digito)

print(f"La suma de los digitos es: {contador}")


# Genera una lista con todos los números primos entre 1 y 100

primos = []

for num in range(2, 101):
    es_primo = True
    
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)
        
print(f"Numeros primos entre 1 y 100: {primos}")

# Imprime la tabla de multiplicar (del 1 al 10) de un número ingresado por el usuario

n = int(input("Ingresa un número: "))

for tabla in range(1, 11):
    print(f"{n} x {tabla} = {n * tabla}")
    
# Dada la lista [1, 2, 3, 2, 4, 5, 1, 6], elimina los duplicados y muestra la lista resultante

lista = [1, 2, 3, 2, 4, 5, 1, 6]
sin_duplicados = []

for numero in lista:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print(f'Lista sin duplicados: {sin_duplicados}')

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