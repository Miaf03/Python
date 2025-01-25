# Escribe un programa que muestre por pantalla la cadena '¡Hola Mundo!'

print("¡Hola Mundo!")

# Escribe un programa que almacene la cadena '¡Hola Mundo!' en una variable y muestre por pantalla el contenido de la variable

cadena = "¡Hola Mundo!"
print(cadena)

# Escribe un programa que pregunte el nombre del usuario y muestre por pantalla la cadena '¡Hola <nombre>!', donde <nombre> es el nombre que el usuario haya intrroducido

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# Escribe un programa que pregunte por el número de horas trabajadas y el coste por hora, después muestra la paga que le corresponde

horas = int(input("Ingresa el número de horas trabajadas: "))
coste = float(input("Ingresa el coste por hora: "))

print(f"Te corresponde una paga de: ${horas * coste:.2f} pesos")

# Escribe un programa que lea un número entero positivo 'n' introducido por el usuario y muestre la suma de todos los enteros desde 1 hasta 'n'

n = int(input("Ingresa un número entero: "))
suma = n * (n + 1) // 2

print(f"La suma de todos los números desde 1 hasta {n} es: {suma}")

# Escribe un programa que pida al usuario su peso en (kg) y estatura en (metros), calcula el índice de masa corporal y almacenalo en una variable y muestra por pantalla la frase: "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal redondeado con dos decimales

peso = float(input("Ingresa tu peso en Kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc = peso / (estatura * estatura)

print(f"Tú indice de masa corporal es {imc:.2f}")

# Escribe un programa que pida al usuario dos números enteros y muestre por pantalla "<n> entre <m> da un cociente de <c> y un resto de <r>" donde <n> y <m> son los números introducidos por el usuario y <c> y <r> son el cociente y el resto de la división

n = int(input("Ingresa un número entero: "))
m = int(input("Ingresa otro número entero: "))

c = n // m
r = n % m

print(f"{n} entre {m} da un cociente de: {c} y un resto de: {r}")

# Escribe un programa que pregunte al usuario la cantidad a invertir, el interes anual y el número de años y muestre por pantalla el capital obtenido en la inversión

inversion = float(input("Cantidad a invertir: "))
interes = float(input("Interes anual: "))
años = int(input("Años a invertir: "))

capital_obtenido = inversion * (interes / 100 + 1) ** años 
print(f"Capital obtenido: ${capital_obtenido:.2f} pesos")

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete asi que debes calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g. Escribe un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviando

peso_payaso = 112
peso_muñeca = 75

payasos_vendidos = int(input("Payasos vendidos en el último pedido: "))
muñecas_vendidas = int(input("Muñecas vendidas en el último pedido: "))

total = peso_payaso * payasos_vendidos + peso_muñeca * muñecas_vendidas
print(f"Peso total del paquete: {total}g")

# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Escribe un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros introducido por el usuario. Después calcula y muestra por pantalla la cantidad de ahorros tras el primer, segundo y tercer año. Rendondea cada cantidad a dos decimales

ahorros = float(input("Dinero depositado en la cuenta de ahorros: "))
interes = 4 / 100 + 1

año1 = ahorros * interes ** 1
año2 = ahorros * interes ** 2
año3 = ahorros * interes ** 3

print(f"Ahorros tras el primer año: ${año1:.2f} pesos")
print(f"Ahorros tras el segundo año: ${año2:.2f} pesos")
print(f"Ahorros tras el tercer año: ${año3:.2f} pesos")

# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total

barras_vendidas = int(input("Ingresa la cantidad de panes vendidos que no son del día: "))
precio = 3.49 
descuento = 60 / 100

costo_final = barras_vendidas * precio * (1 - descuento)

print(f"Precio regular de una barra de pan: {precio:.2f}€")
print(f"Descuento en el pan que no es fresco: {descuento * 100:.0f}%")
print(f"Costo final: {costo_final:.2f}€")