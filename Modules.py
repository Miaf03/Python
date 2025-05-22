# Utiliza el módulo random para generar un número entero aleatorio entre 1 y 100

import random 

entero = random.randint(1, 100)
print(f"Número aleatorio generado: {entero}")


# Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine, dándole pistas de “mayor” o “menor” hasta que acierte.

import random 

numero_aleatorio = random.randint(1, 100)
usuario = int(input("Adivina el número aleatorio (números entre 1 - 100): "))

while usuario != numero_aleatorio:
    
    if usuario > numero_aleatorio:
        print(f"El número es menor que {usuario} ¡Intenta nuevamente!")
        
    elif usuario < numero_aleatorio:
        print(f"El número es mayor que {usuario} ¡Intenta nuevamente!")
    
    usuario = int(input("Adivina el número aleatorio (números entre 1 - 100): "))
    
print(f"¡Haz adivinado!\nNúmero aleatorio: {numero_aleatorio}")
