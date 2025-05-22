"""
    Lista de tareas:

    • Si eliges la opción 1 puedes agregar una tarea
    • Si eliges la opción 2 verás todas las tareas
    • Si eliges la opción 3 puedes marcar una tarea como completada
    • Si eliges la opción 4 puedes eliminar una tarea
    • Si eliges la opción 5 el programa termina
"""

tareas = []

def agregar_tarea(tarea):
    tareas.append({"tarea": tarea, "completada": False})

def mostrar_tareas():
    if not tareas:
        print("\nNo hay tareas en la lista.")
    else:
        for idx, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{idx}. {tarea['tarea']} - {estado}")

def marcar_completada(indice):
    if 0 < indice <= len(tareas):
        tareas[indice - 1]["completada"] = True
        print(f"\nTarea {indice} marcada como completada.")
    else:
        print("Índice inválido.")

def eliminar_tarea(indice):
    if 0 < indice <= len(tareas):
        tareas.pop(indice - 1)
        print(f"Tarea {indice} eliminada.")
    else:
        print("Índice inválido.")

def mostrar_menu():
    print("\n--- Lista de Tareas ---\n")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción:\n\n")
        
        if opcion == "1":
            tarea = input("\nIngresa la nueva tarea: ")
            agregar_tarea(tarea)
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            mostrar_tareas()
            try:
                indice = int(input("\nIngresa el número de la tarea a marcar como completada: "))
                marcar_completada(indice)
            except ValueError:
                print("\nPor favor, ingresa un número válido.")
        elif opcion == "4":
            mostrar_tareas()
            try:
                indice = int(input("\nIngresa el número de la tarea a eliminar: "))
                eliminar_tarea(indice)
            except ValueError:
                print("\nPor favor, ingresa un número válido.")
        elif opcion == "5":
            print("\n¡Hasta luego!\n")
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    ejecutar_programa()
    
    
# Cronometro

import time

def cronometro():
    print("¡Bienvenido al cronómetro!")
    input("Presiona Enter para comenzar...")
    
    tiempo_inicio = time.time()
    
    try:
        while True:
            tiempo_transcurrido = time.time() - tiempo_inicio
            minutos = int(tiempo_transcurrido // 60)
            segundos = int(tiempo_transcurrido % 60)
            milisegundos = int((tiempo_transcurrido * 100) % 100)

            print(f"\033[H\033[J", end="")
            print(f"Tiempo transcurrido: {minutos:02}:{segundos:02}:{milisegundos:02}", end="\r")
            
            time.sleep(0.01)  
    except KeyboardInterrupt:
        
        print("\nCronómetro detenido.")
        total_tiempo = time.time() - tiempo_inicio
        minutos = int(total_tiempo // 60)
        segundos = int(total_tiempo % 60)
        print(f"Tiempo total: {minutos:02}:{segundos:02}")

cronometro()