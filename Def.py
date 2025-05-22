# Escribe una función que cuente cuántos números pares hay en un rango dado por el usuario

def contar_pares(inicio, fin):
    suma = 0

    for numero in range(inicio, fin + 1):
        if numero % 2 == 0: 
            suma += 1
            
    print(f"Hay {suma} números pares entre {inicio} y {fin}")
    
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el final del rango: "))

contar_pares(inicio, fin)
    