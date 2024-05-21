from src.alojamientos import Alojamiento

class CasaODepartamentos(Alojamiento):
    def __init__(self,cantidad_ambientes, direccion):
        self.cantidad_ambientes_por_casa = cantidad_ambientes
        self.direccion = direccion
        super().__init__(self.calcular_precio_alojamiento())
    
        
    def calcular_precio_alojamiento(self):
        if  self.cantidad_ambientes_por_casa == 1:
           return  15000
        elif self.cantidad_ambientes_por_casa >=2 or self.cantidad_ambientes_por_casa <= 4:
            return 30000
        else:
            return 50000
    
