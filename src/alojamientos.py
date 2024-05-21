from src.productos import Productos
from abc import ABC, abstractmethod

class Alojamiento(Productos):
    def __init__(self, direccion):

        self.precio_alojamiento_total = self.calcular_precio_alojamiento()
        self.direccion = direccion
 
    @abstractmethod
    def calcular_precio_alojamiento(self):
        pass
    
    def obtener_direccion(self):
        return self.direccion
    
    def obtener_precio(self):
        return self.precio_alojamiento_total

