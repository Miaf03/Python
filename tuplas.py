# Escribe un programa que recorra una tupla e imprima cada uno de sus elementos en mayúsculas

ciudades = ("cuernavaca", "cdmx", "villahermosa", "huitziltepec")

for ciudad in ciudades:
    print(ciudad.upper())
    
# Crea una tupla con 5 nombres, imprime el primer y el último nombre de la tupla

nombres = ("Uriel", "Yajaira", "Yian", "Dayra", "Yonathan")

print(nombres[0])
print(nombres[-1])

# Crea 2 tuplas una con frutas y otra con verduras. Une ambas tuplas en una nueva tupla e imprimela 

frutas = ("Manzana", "Mango", "Mandarina")
verduras =  ("Chile", "Lechuga", "Aguacate")

union = frutas + verduras
print(union)

# Crea una tupla con varios números repetidos. Usa .count() para contar cuántas veces aparece un número especifico 

numeros = (1, 3, 1, 5, 3, 6, 8, 4, 7, 3, 1)
print(numeros.count(1))

# Crea una lista con 5 elementos. Convierte la lista en una tupla e imprimela

elementos = ["hidrogeno", "helio", "carbono", "nitrogeno", "oxigeno"]
tupla = tuple(elementos)

print(tupla)