
# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Escribe un programa que almacene la cadena 'password' en una variable, luego pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = "password"
password = input("Enter the password: ")

if key == password.lower():
    print("Correct password")
else: 
    print("Incorrect password")

# Escribe un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

n = float(input("Enter the numerator: "))
m = float(input("Enter the denominator: "))

if m == 0:
    print("Error! Division by zero is not allowed")
else:
    print(f"The result is: {n / m:.2f}")
    
# Escribe un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input("Enter your age: "))
income = float(input("Enter your monthly income in euros: "))

if age > 16 and income >= 1000:
    print("You need to pay taxes")
else: 
    print("You don't need to pay taxes")

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

name = input("Enter your name: ")
gender = input("Enter your gender: male/female: ").lower()

if gender == "female" and name[0].upper() < "M":
    print(f"You belong to group A")
elif gender == "male" and name[0].upper() > "N":
    print("You belong to group A")
else:
    print("You belong to group B")

# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

'''
| Renta                 | Tipo Impositivo |
| --------------------- | --------------- |
| Menos de 10000€       | 5%              |
| Entre 10000€ y 20000€ | 15%             |
| Entre 20000€ y 35000€ | 20%             |
| Entre 35000€ y 60000€ | 30%             |
| Más de 60000€         | 45%             |
'''

# Escribe un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

income = float(input("Enter your annnual rental income in euros: "))

if income < 10000:
    tax_rate = 5
elif income <= 20000:
    tax_rate = 15
elif income <= 35000:
    tax_rate = 20
elif income <= 60000:
    tax_rate = 30
else:
    tax_rate = 45

print(f"Your tax rate is {tax_rate}%.")

# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

'''
| Nivel       | Puntuación |
| ----------- | ---------- |
| Inaceptable | 0.0        |
| Aceptable   | 0.4        |
| Meritorio   | 0.6 o más  |
'''

# Escribe un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

score = float(input("Enter your score: "))

if score == 0.0:
    level = "Unacceptable"
elif score == 0.4:
    level = "Acceptable"
elif score >= 0.6:
    level = "Meritorious"
else:
    level = None 

if level:
    money = 2400 * score
    print(f"Performance level: {level}")
    print(f"Money you will receive: {money:.2f}€")
else:
    print("Invalid score. Please enter 0.0, 0.4, or 0.6 or higher.")

# Escribe un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

age = int(input("Enter your age: "))

if age < 4:
    print("You can enter for free")
elif age <= 18:
    print("You must pay 5€")
else:
    print("You must pay 10€")

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribe un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

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
