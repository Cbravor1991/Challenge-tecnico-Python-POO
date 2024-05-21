class Usuario:
    def __init__(self, nombre, presupuesto, productos):
        self.nombre = nombre
        self.presupuesto = presupuesto 
        self.productos = productos # supongo que recibe una lista con productos para simplificar
        
    def contratar_producto(self, producto):
        if producto.obtener_precio() > self.presupuesto:
            print (f"El producto excede el presupuesto")
        else:
            self.presupuesto = self.presupuesto - producto.obtener_precio()
            self.productos.append(producto)
            
    def obtener_cantidad_productos_adquiridos(self):
        return self.productos.count()
    
    def obtener_presupuesto(self):
        return self.presupuesto
    
    
            
        
    