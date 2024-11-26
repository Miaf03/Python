# Ejercicio 1. Escribe un programa que pregunte el nombre del usuario y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Ingrese su nombre: ")
entero = int(input("Ingrese un número entero: "))

print((nombre + "\n") * (entero), end="")

# Ejercicio 2. Escribe un programa que pregunte el nombre completo del usuario y muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre_completo = input("Escribe tu nombre completo: ")

print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.title())

# Ejercicio 3. Escribe un programa que pregunte el nombre del usuario y después muestre por pantalla "<NOMBRE> tiene <n> letras" donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el nombre.

nombre = input("Ingrese su nombre: ")
n = len(nombre)

print(f"{nombre.upper()} tiene {n} letras")

# Ejercicio 4. Los teléfonos de una empresa tienen el siguiente formato 'prefijo-número-extension' donde el prefijo es el código del país '+34', y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribe un programa que pregunte por un número de télefono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

tel = (input("Ingrese un número de telefono con el formato +xx-xxxxxxxxxx-xx: "))
print(f"El número de teléfono es: {tel[4:-3]}")

# Ejercicio 5. Escribe un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input("Ingrese una frase: ")
print(f"frase invertida: {frase[::-1]}")

# Ejercicio 6. Escribe un programa que pida al usuario que introduzca una frase en la consola y una vocal, después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")

print(frase.replace(vocal, vocal.upper()))

# Ejercicio 7. Escribe un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio 'ceu.es'. 

email = input("Ingrese su correo electronico: ")
print(f"{email[:email.find("@")]}@ceu.es")

# Ejercicio 8. Escribe un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestre por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.



# Ejercicio 9. Escribe un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.



# Ejercicio 10. Escribe un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


