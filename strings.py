
# Ejercicio 1. Escribe un programa que pregunte el nombre del usuario y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

name = input("Enter your name: ")
integer = int(input("Enter an integer: "))

print((name + "\n") * (integer), end="")

'''end="" Es un argumento de la función print() que controla como termina la salida'''


# Ejercicio 2. Escribe un programa que pregunte el nombre completo del usuario y muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.

name = input("Enter your full name: ")

print(name.lower())
print(name.upper())
print(name.title())


# Ejercicio 3. Escribe un programa que pregunte el nombre del usuario y después muestre por pantalla "<NAME> tiene <n> letras" donde <NAME> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el nombre.

name = input("Enter your name: ")
n = len(name.replace(" ", "")) # Elimina espacios antes de contar
print(f"{name.upper()} has {n} letters")


# Ejercicio 4. Los teléfonos de una empresa tienen el siguiente formato 'prefijo-número-extension' donde el prefijo es el código del país '+34', y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribe un programa que pregunte por un número de télefono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

tel = input("Enter a phone number in the format +xx-number-extension: ")
parts = tel.split('-')

print(f"The phone number without the prefix or extension is: {parts[1]}")

'''
Cuando usamos split('-'), estamos dividiendo el número en tres partes, el guion (-) lo usamos como separador. La parte del número (sin prefijo ni extensión) está en el índice 1 de la lista.
'''


# Ejercicio 5. Escribe un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

phrase = input("Enter a phrase: ")
print(f"The reversed phrase is: {phrase[::-1]}")


# Ejercicio 6. Escribe un programa que pida al usuario que introduzca una frase en la consola y una vocal, después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

phrase = input("Enter a phrase: ")
vowel = input("Enter a vowel: ")

print(phrase.replace(vowel, vowel.upper()))


# Ejercicio 7. Escribe un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio 'ceu.es'. 

email = input("Enter your email: ")
parts = email.split("@")

print(f"{parts[0]}@ceu.es")


# Ejercicio 8. Escribe un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestre por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

date = input("Enter your birthdate in the format dd/mm/yyyy: ")
day, month, year = date.split('/')
day = day.zfill(2)
month = month.zfill(2)
  
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")

'''Método zfill(n) si el string es más corto que 'n' agrega ceros al principio hasta que su logitud sea de n caracteres'''


# Ejercicio 9. Escribe un programa que pregunte por consola por los productos de una cesta, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

products = input("Enter the products in the basket separated by commas: ")
basket = products.split(',')

print("\n".join(basket))
