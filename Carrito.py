import os 
# Esta es la clase Carrito, aqui es donde definimos que propiedades
# tiene el carrito, en este caso lo que va a tener es una lista de productos
# donde vamos a ir almacenando los productos que el usuario va agregando.
class Carrito:
  # Atributos:
  def __init__(self):
    self.productos = []
  
  # Metodos:
  
  # Este metodo nos permite ir agregando un prodcuto a la lista de productos
  def agregar_producto(self, producto):
    self.productos.append(producto)

  # Este nos va a retornar el total de la suma de todos los productos con 
  # sus cantidades.  
  def calcular_total(self):
    return sum(producto.subtotal() for producto in self.productos)
  
  # Con este metodo es donde generamos el recibo de la compra
  def generar_recibo(self, ruta):
    # Verificamos si la carpeta existe, si no existe la creamos
    os.makedirs("./compras", exist_ok=True)
    # Aqui abrimos el archivo en modo append, para que no se borre lo que ya hay.
    with open(ruta, "w") as archivo:
      archivo.write("Recibo de compra:\n")
      archivo.write("-" * 45 + "\n")
      # Aqui iteramos por cada producto en la lista de productos y escribimos
      # la info de cada producto en el archivo
      for producto in self.productos:
        archivo.write(f"Producto: {producto.nombre}, Precio: c{producto.precio}, Cantidad: {producto.cantidad}\n")
        archivo.write("-" * 45 + "\n")
      print("-" * 45)
      archivo.write(f"Total: c{self.calcular_total()}")
      archivo.flush() # Esto es para que se escriba el archivo inmediatamente (aveces no lo hace)
    
  # En este metodo leemos el archivo y lo mostramos al usuario. Este ya tiene 
  # el manejo de errores, en caso de que el archivo no exista. Entonces le 
  # decimos al usuario que debe generar un recibo antes.
  def leer_recibo(self, ruta):
    try:
      with open(ruta, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print("El archivo no existe. Debe generar un recibo antes.")
        
  def eliminar_recibo(self, ruta):
    try:
      os.remove(ruta)
    except Exception as e:
        print(f"Error elminando el recibo anterior... {e}")
 
    
# Con este metodo nos encargamos de mostrar el carrito de comprars al usuario.
  def mostrar_carrito(self):
    print("\nCarrito de compras:")
    for producto in self.productos:
      print("-" * 25)
      print("\nProducto: ", producto.nombre, "\nPrecio: ₡", producto.precio, "\nCantidad: ", producto.cantidad)
      
    print("-" * 25)
    print("\nTotal: ₡", self.calcular_total())
  
  
  