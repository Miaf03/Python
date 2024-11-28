
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

# Ejercicio 6. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingresa tu nombre: ")
genero = input("Ingresa tu sexo: (hombre/mujer): ").lower()

if genero == "mujer" and nombre[0].upper() < "M":
    print(f"Perteneces al grupo A")
elif genero == "hombre" and nombre[0].upper() > "N":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

# Ejercicio 7. Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

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

renta = float(input("Ingresa tu rental anual en euros: "))

if renta < 10000:
    tipo = 5
elif renta <= 20000:
    tipo = 15
elif renta <= 35000:
    tipo = 20
elif renta <= 60000:
    tipo = 30
else:
    tipo = 45

print(f"Tu tipo impositivo es del {tipo}%.")

# Ejercicio 8. En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

'''
| Nivel       | Puntuación |
| ----------- | ---------- |
| Inaceptable | 0.0        |
| Aceptable   | 0.4        |
| Meritorio   | 0.6 o más  |
'''

# Escribe un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

puntuacion = float(input("Ingrese su puntuación: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion == 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None 

if nivel:
    dinero = 2400 * puntuacion
    print(f"Nivel de rendimiento: {nivel}")
    print(f"Dinero que recibirá: {dinero:.2f}€")
else:
    print("Puntuación no válida. Por favor, ingrese 0.0, 0.4, o 0.6 o más.")

# Ejercicio 9. Escribe un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("Ingresa tu edad: "))

if edad < 4:
    print("Puedes entrar gratis")
elif edad <= 18:
    print("Debes pagar 5€")
else:
    print("Debes pagar 10€")
