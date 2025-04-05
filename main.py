from Producto import Producto
from Carrito import Carrito

import os
import time

# Diccionario productos
productos = {
  "pan": 850,
  "leche": 1200,
  "arroz": 2500,
  "huevos": 1800,
  "azúcar": 1400,
  "sal": 500,
  "aceite": 3500,
  "café": 4500,
  "harina": 1200,
  "queso": 3200
}

carrito = Carrito()

# Possible options:
# 1. Seleccionar producto
# 2. Ver carrito
# 3. Generar recibo

while True:
  # Bienvenida al usuario
  os.system("cls")
  print("-" * 30)
  print("Bienvenido a la tienda virtual")
  print("-" * 30)

  # Mostrar los productos con los precios ✅
  print("\nProductos disponibles:\n")
  i = 0
  print("-" * 25)
  for i, (producto, precio) in enumerate(productos.items(), 1):
    print(f"{i}. {producto.capitalize()} - ₡{precio}")
  print("-" * 25)
  
  #TODO: Mostrar el menu:
  print("\n1. Seleccionar producto")
  print("2. Ver carrito")
  print("3. Generar recibo")
  opcion_menu = input('\nSeleccione una opcion o escriba "salir" para salir del sistema: ')
  
  match opcion_menu:
    case "1":
      # Seleccionar un producto por número ✅
      opcion_producto = input('\nSeleccione un producto: ')
      producto_elegido = list(productos.keys())[int(opcion_producto) - 1]
      precio = productos[producto_elegido]
      cantidad = int(input(f"\nIngrese la cantidad de {producto_elegido}: "))

      # Instanciar el objeto Producto ✅
      producto = Producto(producto_elegido.capitalize(), precio, cantidad)
      # Agregar el producto al carrito ✅
      carrito.agregar_producto(producto)
      
      print("Producto agregado al carrito")
      input("\nPresione ENTER para continuar...")
    
    case "2":
      carrito.mostrar_carrito()
      input("\nPresione ENTER para continuar...")
      
    case "salir":
      print("Saliendo del sistema...")
      time.sleep(1)
      exit()
    case _:
      print("Por favor, seleccione una opción válida")
      time.sleep(1)
      continue