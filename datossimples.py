
# Escribe un programa que muestre por pantalla la cadena 'Hello World!'.

print("Hello World!")

# Escribe un programa que almacene la cadena 'Hello World!' en una variable y muestre por pantalla el contenido de la variable.

cadena = "Hello World!"
print(cadena)

# Escribe un programa que pregunte el nombre del usuario en la consola y muestre por pantalla la cadena 'Hello <name>!', donde <name> es el nombre que el usuario haya intrroducido.

name = input("Enter your name: ")
print(f"Hello {name}!")

# Escribe un programa que pregunte por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

hours = int(input("Enter the number of hours worked "))
rate = float(input("Enter the cost per hour: "))

print(f"You are entitled to a payment of ${hours * rate:.2f} pesos")

# Escribe un programa que lea un entero positivo 'n' introducido por el usuario y luego muestre por pantalla la suma de todos los enteros desde 1 hasta 'n'.

n = int(input("Enter an integer: "))
sum = n * (n + 1) // 2

print(f"The sum of all integers from 1 to {n} is: {sum}")

# Escribe un programa que pida al usuario su peso en (kg) y estatura en (metros), calcula el índice de masa corporal y almacenalo en una variable y muestra por pantalla la frase: "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal redondeado con dos decimales.

weight = float(input("Ingrese su peso en kg: "))
height = float(input("Ingrese su estatura en metros: "))

bmi = weight / (height * height)
print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")

# Escribe un programa que pida al usuario dos números enteros y muestre por pantalla "<n> entre <m> da un cociente de <c> y un resto de <r>" donde <n> y <m> son los números introducidos por el usuario y <c> y <r> son el cociente y el resto de la división.

n = int(input("Enter an integer: "))
m = int(input("Enter another integer: "))

c = n // m
r = n % m

print(f"{n} divided by {m} gives a quotient of: {c} and a remainder of: {r}")

# Escribe un programa que pregunte al usuario la cantidad a invertir, el interes anual y el número de años y muestre por pantalla el capital obtenido en la inversión.

investment = float(input("Amount to invest: "))
interest = float(input("Annual interest rate: "))
years = int(input("Years to invest: "))

obtained_capital = investment * (interest / 100 + 1) ** years 
print(f"Obtained capital: ${obtained_capital:.2f} pesos")

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete asi que debes calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g. Escribe un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviando.

clown_weight = 112
doll_weight = 75

clowns_sold = int(input("Clowns sold in the last order: "))
dolls_sold = int(input("Dolls sold in the last order: "))

total_weight = clown_weight * clowns_sold + doll_weight * dolls_sold
print(f"The total package weight is: {total_weight}g")

# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Escribe un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros introducido por el usuario. Después calcula y muestra por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Rendondea cada cantidad a dos decimales.

savings = float(input("Money deposited in the savings account: "))
interest = 4 / 100 + 1

year1 = savings * interest ** 1
year2 = savings * interest ** 2
year3 = savings * interest ** 3

print(f"Savings after the first year: ${year1:.2f} pesos")
print(f"Savings after the second year: ${year2:.2f} pesos")
print(f"Savings after the third year: ${year3:.2f} pesos")

# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

sold_leaves = int(input("Enter the number of sold loaves that are not fresh: "))
price = 3.49 
discount = 60 / 100

final_cost = sold_leaves * price * (1 - discount)

print(f"Regular price of a loaf of bread: {price:.2f}€")
print(f"Discount on a non-fresh loaf: {discount * 100:.0f}%")
print(f"Final cost: {final_cost:.2f}€")