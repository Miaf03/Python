    
# Pide al usuario que escriba una contraseña hasta que acierte

contraseña = "python123"
key = input("Ingresa la contraseña correcta: ")

while key != contraseña:
       print("Vuelve a intentarlo")
       key = input("Ingresa la contraseña correcta: ")
       
print("Contraseña correcta")

'''
Descripción: Eres el dueño de una tienda, tienes un inventario con productos y precios. El cliente elige productos y los va agregando a su carrito. Al pagar, se le muestra el total y se genera un código aleatorio de confirmación, el cliente puede:

	1.	Ver productos
	2.	Comprar producto
	3.	Ver carrito
	4.	Pagar
	5.	Salir
'''

import random

inventario = {
    "poción de vida": 50,
    "espada mágica": 120,
    "escudo protector": 100,
    "anillo de invisibilidad": 200
}

carrito = []

while True:
    print("\n Bienvenido a la Tienda Mágica\n")
    print("--- Menú: ---\n")
    print("[1] Ver productos")
    print("[2] Comprar producto")
    print("[3] Ver carrito")
    print("[4] Pagar")
    print("[5] Salir")

    opcion = input("\nElige una opción del 1 al 5:\n\n")

    if opcion == "1":
        print("\n📦 Productos disponibles:\n")
        for producto, precio in inventario.items():
            print(f"- {producto}: ${precio}")

    elif opcion == "2":
        producto = input("\n¿Qué producto deseas comprar?:\n\n").lower()

        if producto in inventario:
            carrito.append(producto)
            print(f"\n✅ '{producto}' agregado al carrito\n")
        else:
            print("\n❌ Ese producto no existe en la tienda\n")

    elif opcion == "3":
        if carrito:
            print("\n🛒 Tu carrito contiene:\n")
            for item in carrito:
                print(f"- {item} (${inventario[item]})")
        else:
            print("\n🛒 El carrito está vacío\n")

    elif opcion == "4":
        if carrito:
            total = 0
            for item in carrito:
                total += inventario[item]
            print(f"\n💰 Total a pagar: ${total}")
            codigo = random.randint(1000, 9999)
            print(f"\n🎉 Gracias por tu compra. Tu código mágico es: {codigo}\n")
            carrito.clear()
        else:
            print("❌ No puedes pagar porque el carrito está vacío.")

    elif opcion == "5":
        print("\n👋 ¡Gracias por visitar la Tienda Mágica!\n")
        break

    else:
        print("\n⚠️ Opción no válida. Intenta otra vez\n")