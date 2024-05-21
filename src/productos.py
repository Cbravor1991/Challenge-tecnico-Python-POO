from abc import ABC, abstractmethod

class Productos(ABC):
    @abstractmethod
    def obtener_precio(self):
        '''Devuelve el precio de la propiedad'''
        pass
    

   