# Escribe un programa que almacene las asignaturas: Matemáticas, Física, Química e Historia en una lista y muestre por pantalla el mensaje 'Yo estudio <asignatura>' donde <asignatura> es cada una de las asignaturas de la lista

asignaturas = ["Matemáticas", "Física", "Química", "Historia"]

for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")

# Escribe un programa que pregunte por los productos de una cesta, separados por comas y muestre por pantalla cada uno de los productos en una línea distinta. (strip() elimina los espacios extra de al principio y al final del elemento)

productos = input("Ingresa el nombre de los productos de la cesta separados por comas: ")
cesta = productos.split(",")

cesta = [producto.strip() for producto in cesta]
print("\n".join(cesta))