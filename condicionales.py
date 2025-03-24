# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor o menor de edad

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Escribe un programa que pida al usuario dos números y muestre por pantalla su división si el divisor es cero el programa debe mostrar un error

n = float(input("Ingresa el númerador: "))
m = float(input("Ingresa el denominador: "))

if m == 0:
    print("¡Error! No se puede dividir por cero")
else:
    print(f"El resultado es: {n / m:.2f}")
    
# Escribe un programa que pida al usuario un número y muestre si es par o impar

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a $1000 pesos MXN mensuales. Escribe un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre si el usuario tiene que tributar o no

edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    print("Tienes que pagar impuestos")
else: 
    print("No debes pagar impuestos")
    
# Pide al usuario un número y verifica si ese número está en la lista [2, 4, 6, 8, 10]

numero = int(input("Ingresa un número: "))
lista = [2, 4, 6, 8, 10]
    
if numero in lista:
    print(f"{numero} esta dentro de la lista {lista}")
else: 
    print(f"{numero} no esta dentro de la lista {lista}")    

# Los alumnos de un curso se han dividido en dos grupos. A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde

nombre = input("Ingresa tu nombre: ")
genero = input("Ingresa tu género: hombre/mujer: ").lower()

if genero == "mujer" and nombre[0].upper() < "M":
    print(f"Perteneces al grupo A")
elif genero == "hombre" and nombre[0].upper() > "N":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

# La pizzería Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación:

# Ingredientes vegetarianos: Pimiento y tofu
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón

# Escribe un programa que pregunte al usuario si quiere una pizza vegetariana o no y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva

tipo = input("Ingresa 1 para una pizza vegetariana o ingresa 2 para una pizza no vegetariana: ")
ingredientes_base = "mozzarella, tomate"

if tipo == "1":
    print("Ingredientes de pizzas vegetarianas:\n1. Pimiento\n2. Tofu")
    ingrediente = input("Introduce el número del ingrediente que deseas (1 o 2): ")
    
    if ingrediente == "1":
        ingrediente_elegido = "pimiento"
    elif ingrediente == "2":
        ingrediente_elegido = "tofu"
    else:
        ingrediente_elegido = "opción inválido"
    
    print(f"Pizza vegetariana con {ingredientes_base} y {ingrediente_elegido}.")
    
elif tipo == "2":
    print("Ingredientes de pizzas no vegetarianas:\n1. Peperoni\n2. Jamón\n3. Salmón")
    ingrediente = input("Introduce el número del ingrediente que deseas (1, 2 o 3): ")
    
    if ingrediente == "1":
        ingrediente_elegido = "peperoni"
    elif ingrediente == "2":
        ingrediente_elegido = "jamón"
    elif ingrediente == "3":
        ingrediente_elegido = "salmón"
    else:
        ingrediente_elegido = "opción inválido"
    
    print(f"Pizza no vegetariana con {ingredientes_base} y {ingrediente_elegido}.")
    
    
# Pide al usuario una palabra y verifica si es un palíndromo (se lee igual de adelante hacia atrás)
    
palabra = input("Ingresa una palabra: ").replace(" ", "").lower()

if palabra.isalpha():
    if palabra == palabra[::-1]:
        print(f"{palabra} es un palíndromo")
    else:
        print("No es un palíndromo")
else:
    print("Por favor, ingresa solo letras")
    
# Pide al usuario una letra y muestra el índice de su primera aparición en el texto "Python es genial"

letra = input("Ingresa una letra: ")
texto = "Python es genial"

if letra in texto:
    aparicion = texto.index(letra)
    print(f'Indice de la primera aparición de la letra "{letra}" en "{texto}": {aparicion}')
else: 
    print(f'La letra "{letra}" no se encuentra en el texto: "{texto}"')
    

# Calculadora: Crea un programa que solicite dos números al usuario y permita realizar operaciones de suma, resta, multiplicación y división     

a = float(input("Ingresa un número: "))
b = float(input("Ingresa otro número: "))

if a == int(a):
    resultado_a = f"{int(a)}"
else:
    resultado_a = f"{a:.2f}"

if b == int(b):
    resultado_b = f"{int(b)}"
else:
    resultado_b = f"{b:.2f}"

operacion = input("\n¿Qué operación deseas realizar ingresa:\n\n(+) para sumar\n(-) para restar\n(*) para multiplicar\n(/) para dividir:\n\n")

if operacion == "+":
    resultado = a + b
elif operacion == "-":
    resultado = a - b
elif operacion == "*":
    resultado = a * b
elif operacion == "/":
    if b != 0:
        resultado = a / b
    else: 
        print("¡Error! No se puede dividir por 0")
else:
    print("¡Error! Ingresa uno de los siguiente operadores: +, -, *, /")
    exit()
    
if resultado == int(resultado):
    resultado = int(resultado)
else:
    resultado = f"{resultado:.2f}"
    
print(f"El resultado de {resultado_a} {operacion} {resultado_b} es {resultado}")