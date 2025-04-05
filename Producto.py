# Esta es la clase producto, aqui es donde definimos que propiedades
# tiene el producto y sus metodos (funciones que puede realizar).
class Producto:
  # Atributos:
  def __init__(self, nombre, precio, cantidad):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
    
    
  # Metodos:
  
  # Retorna el subtotal del producto, o sea el precio por la cantidad. Para asi
  # despues poder calcular el total de la compra.
  def subtotal(self):
    return self.precio * self.cantidad
  
  # Este metodo es especial, ya que cuando le hacemos un print a un objeto
  # normalmente lo que imprime es la direccion de memoria donde se encuentra 
  # el objeto. Entonces con este metodo le decimos que queremos que imprima 
  # la info del objeto.
  def __str__(self):
    return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
  
  