# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Escribe un programa que almacene la cadena 'password' en una variable, pregunte al usuario por la contraseña e imprima si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas

key = "password"
contraseña = input("Ingresa la contraseña: ")

if key == contraseña.lower():
    print("Contraseña correcta")
else: 
    print("Contraseña incorrecta")

# Escribe un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error

n = float(input("Ingresa el númerador: "))
m = float(input("Ingresa el denominador: "))

if m == 0:
    print("¡Error! No se puede dividir por cero")
else:
    print(f"El resultado es: {n / m:.2f}")
    
# Escribe un programa que pida al usuario un número entero y muestre por pantalla si es par o impar

numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 pesos mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no

edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    print("Tienes que pagar impuestos")
else: 
    print("No debes pagar impuestos")

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde

nombre = input("Ingresa tu nombre: ")
genero = input("Ingresa tu género: hombre/mujer: ").lower()

if genero == "mujer" and nombre[0].upper() < "M":
    print(f"Perteneces al grupo A")
elif genero == "hombre" and nombre[0].upper() > "N":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

# Escribe un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años 10€

edad = int(input("Ingresa tu edad: "))

if edad < 4:
    print("Puedes entrar gratis")
elif edad <= 18:
    print("Debes pagar 5€")
else:
    print("Debes pagar 10€")

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación

# Ingredientes vegetarianos: Pimiento y tofu
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón

# Escribe un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva

tipo = input("Ingresa 1 para una pizza vegetariana e ingresa 2 para una pizza no vegetariana: ")
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