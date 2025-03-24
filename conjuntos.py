# Crea un conjunto con 5 números, agrega un nuevo número y  elimina otro número e imprímelo

conjunto = {2, 5, 7, 3, 9}
print(conjunto)

conjunto.add(21)
print(conjunto)

conjunto.remove(2)
print(conjunto)

# Declara dos conjuntos con diferentes animales. Une ambos conjuntos en uno solo

a = {"leon", "tortuga", "pajaro"}
b = {"raton", "cucaracha", "mariposa"}

union = a | b
print(union)


# Declara dos conjuntos con colores (algunos en común encuentra los colores que tienen en común e imprímelos

a = {"azul", "morado", "naranja", "rosa"}
b = {"verde", "rosa", "rojo", "turquesa"}

colores_comunes =  a & b
print(colores_comunes)


# Declara dos conjuntos con algunos números en común. Muestra los elementos que están en el primer conjunto pero no en el segundo

numero_1 = {1, 3, 5, 6, 7, 8}
numero_2 = {1, 2, 4, 5, 6, 9}

diferencia = numero_1 - numero_2
print(diferencia)