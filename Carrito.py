import os 

class Carrito:
  def __init__(self):
    self.productos = []
  
  def agregar_producto(self, producto):
    self.productos.append(producto)
  
  def calcular_total(self):
    return sum(producto.precio for producto in self.productos)
      
  def generar_recibo(self, ruta):
    # Verificar si la carpeta "datos" existe, y si no, la crea
    os.makedirs("./compras", exist_ok = True)

    # Usa el archivo con "a" de append para poder escribir en
    # el archivo sin que se sobreescriba.
    with open("./compras/recibo.txt", "a") as archivo:
      archivo.write(f"")
      archivo.flush()  # Forzar escritura inmediata
      
  def mostrar_carrito(self):
    print("Carrito de compras:")
    for producto in self.productos:
      print("\nProducto: ", producto.nombre, "\nPrecio: ", producto.precio, "\nCantidad: ", producto.cantidad)
    print("\nTotal: ₡", self.calcular_total())
  
  
  