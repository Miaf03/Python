# Ejercicio 1. Escribe un programa que pregunte el nombre del usuario y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Ingrese su nombre: ")
entero = int(input("Ingrese un número entero: "))

print((nombre + "\n") * (entero), end="")

'''end="" Es un argumento de la función print() que controla como termina la salida'''

# Ejercicio 2. Escribe un programa que pregunte el nombre completo del usuario y muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.

nombre_completo = input("Escribe tu nombre completo: ")

print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.title())

# Ejercicio 3. Escribe un programa que pregunte el nombre del usuario y después muestre por pantalla "<NOMBRE> tiene <n> letras" donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tiene el nombre.

nombre = input("Ingresa tu nombre: ")
n = len(nombre.replace(" ", "")) # Elimina espacios antes de contar
print(f"{nombre.upper()} tiene {n} letras")

# Ejercicio 4. Los teléfonos de una empresa tienen el siguiente formato 'prefijo-número-extension' donde el prefijo es el código del país '+34', y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribe un programa que pregunte por un número de télefono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

tel = input("Ingrese un número de teléfono con el formato '+xx-número-extensión': ")
partes = tel.split('-')
numero = partes[1]

print(f"El número de teléfono sin prefijo ni extensión es: {numero}")

'''
Cuando usamos split('-'), estamos dividiendo el número en tres partes, el guion (-) lo usamos como separador. La parte del número (sin prefijo ni extensión) está en el índice 1 de la lista.
'''

# Ejercicio 5. Escribe un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input("Ingrese una frase: ")
print(f"La frase invertida es: {frase[::-1]}")

# Ejercicio 6. Escribe un programa que pida al usuario que introduzca una frase en la consola y una vocal, después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")

print(frase.replace(vocal, vocal.upper()))

# Ejercicio 7. Escribe un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio 'ceu.es'. 

email = input("Ingrese su correo electronico: ")
correo = email.split("@")

print(f"Email: {correo[0]}@ceu.es")

# Ejercicio 8. Escribe un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestre por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, año = fecha.split('/')
dia = dia.zfill(2)
mes = mes.zfill(2)
  
print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {año}")

'''Método zfill(n) si el string es más corto que 'n' agrega ceros al principio hasta que su logitud sea de n caracteres'''

# Ejercicio 9. Escribe un programa que pregunte por consola por los productos de una cesta, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos = input("Ingrese los productos de la cesta separados por comas: ")
cesta = productos.split(',')

print("\n".join(cesta))