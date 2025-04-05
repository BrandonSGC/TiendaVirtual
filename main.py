from Producto import Producto
from Carrito import Carrito

import os
import time

# Diccionario productos disponibles.
# Un diccionario es una estructura de datos que nos 
# permite almacenar info en pares de clave-valor.
# Por ejemplo, una clave seria "pan" y su valor seria 850.
# En Python y muchos otros lenguajes, los diccionarios son
# estructuras de datos muy utiles, ya que nos permiten
# almacenar info de una manera muy ordenada y facil de acceder.
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

# Instanciar el objeto Carrito.
# Lo instanciamos fuera del while para que no se reinicie el
# carrito cada vez que el usuario escoja una opcion del menu.
carrito = Carrito()

# Limpiar el archivo de recibo si existe.
# Esto es para que no quede datos de recibos pasados en el sistema.
carrito.eliminar_recibo("./compras/recibo.txt")

# Este while es el que nos permite mostrar el menu siempre hasta
# que el usuario decida salir del sistema.
while True:
  # Bienvenida al usuario
  os.system("cls")
  print("-" * 30)
  print("Bienvenido a la tienda virtual")
  print("-" * 30)

  # Mostrar los productos con los precios
  print("\nProductos disponibles:\n")
  i = 0
  print("-" * 25)
  for i, (producto, precio) in enumerate(productos.items(), 1):
    print(f"{i}. {producto.capitalize()} - ₡{precio}")
  print("-" * 25)
  
  # Mostrar el menu:
  print("\n1. Seleccionar producto")
  print("2. Mostrar carrito")
  print("3. Generar recibo")
  print("4. Mostrar recibo")
  opcion_menu = input('\nSeleccione una opcion o escriba "salir" para salir del sistema: ')
  
  # Este es el match que le decia, es lo mismo que un if-elif-else pero esta
  # es la manera recomendada y moderna de hacerlo en Python.
  match opcion_menu:
    case "1":
      # Seleccionar un producto por número
      opcion_producto = input('\nSeleccione un producto: ')
      producto_elegido = list(productos.keys())[int(opcion_producto) - 1]
      precio = productos[producto_elegido]
      cantidad = int(input(f"\nIngrese la cantidad de {producto_elegido}: "))

      # Instanciar el objeto Producto. Recuerde que aqui es cuando creamos un 
      # objeto de la clase Producto, y le pasamos los atributos que definimos
      # en la clase producto (nombre, precio y cantidad).
      producto = Producto(producto_elegido.capitalize(), precio, cantidad)
      
      # Una vez hecho el producto lo vamos a agregar al carrito
      carrito.agregar_producto(producto)
      
      print("Producto agregado al carrito")
      input("\nPresione ENTER para continuar...")
    
    case "2":
      carrito.mostrar_carrito()
      input("\nPresione ENTER para continuar...")
      
    case "3":
      # Validar si no tiene productos en el carrito
      if not carrito.productos:
        print("No tiene productos en el carrito")
        input("\nPresione ENTER para continuar...")
        continue
      
      # Generar el recibo
      carrito.generar_recibo("./compras/recibo.txt")
      print("\nRecibo generado con éxito")
      input("\nPresione ENTER para continuar...")
      
    case "4":
      # Con el objeto carrito, llamamos al metodo leer_recibo para mostrarle el
      # recibo al usuario con los productos que ha comprado.
      carrito.leer_recibo("./compras/recibo.txt")
      input("\nPresione ENTER para continuar...")
      
    # Si el usuario ingresa "salir" entonces se va a salir del sistema.
    case "salir":
      print("Saliendo del sistema...")
      # Aqui le pongo un segundo de tiempo hasta que se salga como para que de la
      # sensacion de que esta saliendose, pero puede quitarlo si quiere.
      time.sleep(1) 
      exit()
      
    # Si el usuario no ingresa una opcion valida, entonces le decimos que escoja
    # una opcion valida
    case _:
      print("Por favor, seleccione una opción válida")
      time.sleep(1)
      continue
    

# Cosas por hacer:

# - Manejo de errores (try-except) para evitar que el usuario ingrese un valor no valido en los menus o a la hora de escoger productos y que no se le despiche el
# programa.

# - Probar el sistema, pruebe e intente realizar todos los posibles escenarios
# porque siepmre a uno se le van errores o validaciones por hacer...

# - Aunque es opcional, podria intentar hacer los extras opcionales para que tenga
# mas puntos pero si puede ser un poco complicado al principio para usted porque
# no ha trabajado mucho con este paradigma de programacion.