
# Ejercicio 1. Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingresa tu edad: "))

if edad <= 17:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad") 

# Ejercicio 2. Escribe un programa que almacene la cadena 'contraseña' en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = "contraseña"
password = input("Ingresa la contraseña: ")

if key == password.lower():
    print("La contraseña coincide")
else: 
    print("La contraseña no coincide")

# Ejercicio 3. Escribe un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

n1 = float(input("Introduce el dividendo: "))
n2 = float(input("Introduce el divisor: "))

if n2 == 0:
    print("¡Error! No se puede dividir por 0")
else:
    print(f"El resultado de la división es: {n1 / n2:.2f}")
    