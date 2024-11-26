
# Ejercicio 1. Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejercicio 2. Escribe un programa que almacene la cadena 'contraseña' en una variable, luego pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = "contraseña"
password = input("Ingresa la contraseña: ")

if key == password.lower():
    print("Contraseña correcta")
else: 
    print("Contraseña incorrecta")

# Ejercicio 3. Escribe un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

n = float(input("Ingresa el numerador: "))
m = float(input("Ingresa el denominador: "))

if m == 0:
    print("¡error!, no se puede dividir entre cero")
else:
    print(f"El resultado es: {n / m:.2f}")
    
# Ejercicio 4. Escribe un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicio 5. Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Agrega tus ingresos mensuales en euros: "))

if edad > 16 and ingresos >= 1000:
    print("Tienes que tributar")
else: 
    print("No tienes que tributar")
