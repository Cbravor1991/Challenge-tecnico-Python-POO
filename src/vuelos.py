from src.productos import Productos

class Vuelos(Productos):
    def __init__(self, precio_establecido, fecha_ida, fecha_vuelta =0):
        self.precio_establecido = precio_establecido
        self.fecha_ida = fecha_ida
        self.fecha_vuelta = fecha_vuelta
    
    
    def obtener_fecha_ida(self):
        return self.fecha_ida
        
    def obtener_fecha_vuelta(self):
        return self.fecha_vuelta
    
    def obtener_precio(self):
        return self.precio_establecido
        