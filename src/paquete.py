from src.productos import Productos

class Paquete(Productos):
    def __init__(self):
        self.precio_total = 0
        self.productos = []
        
    def agregar_producto (self, producto):
        self.productos.append(producto)
        
    def calcular_precio(self):
        if self.productos:
            for producto in self.productos:
                self.precio_total += producto.obtener_precio()
            
    def obtener_precio(self):
        self.calcular_precio()
        return self.precio_total
