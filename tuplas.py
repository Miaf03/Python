# Escribe un programa que recorra una tupla e imprima cada uno de sus elementos en mayúsculas

ciudades = ("Cuernavaca", "CDMX", "Villahermosa", "Guadalajara")

for ciudad in ciudades:
    print(ciudad.upper())
    
# Crea una tupla con 5 nombres e imprime el primer y el último nombre de la tupla

nombres = ("Uriel", "Yajaira", "Yian", "Dayra", "Yonathan")

print(nombres[0])
print(nombres[-1])

# Crea 2 tuplas una con frutas y otra con verduras y une ambas en una nueva tupla

frutas = ("Manzana", "Mango", "Mandarina")
verduras =  ("Chile", "Lechuga", "Aguacate")

union = frutas + verduras
print(union)

# Crea una lista con 5 elementos. Convierte la lista en una tupla e imprimela

elementos = ["hidrogeno", "helio", "litio", "berilio", "boro"]
tupla = tuple(elementos)

print(tupla)