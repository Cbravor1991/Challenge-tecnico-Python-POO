from src.alojamientos import Alojamiento

class Hoteles(Alojamiento):
    def __init__(self, nombre, cantidad_estrella, direccion):
        self.nombre = nombre
        self.cantidad_estrella = cantidad_estrella
        self.precio_fijo_noche = 10000
        super().__init__(self.calcular_precio_alojamiento(), direccion)
    
        
        
    def calcular_precio_alojamiento(self):
        return self.precio_fijo_noche * self.cantidad_estrella
    


    def obtener_nombre(self):
        return self.nombre
    
