from src.casaDepartamento import CasaODepartamentos

class Cabañas(CasaODepartamentos):
    def __init__(self, direccion, cantidad_casas_alquilar, cantidad_ambientes=0):
        super().__init__(cantidad_ambientes, direccion)
        self.cantidad_casas_alquilar = cantidad_casas_alquilar
        self.casas_componen_cabañas = []
      
    
    def agregar_casas (self, casa):
        self.casas_componen_cabañas.append(casa)
        
    def calcular_precio_alojamiento(self):
        '''calcula precio alojamiento segun descuento'''
        if self.cantidad_casas_alquilar > self.casas_componen_cabañas.count(): 
            descuento_porcentaje = min(50, 10 * self.cantidad_casas_alquilar)
            for i in range (1, self.cantidad_casas_alquilar+1):
                precio = self.casas_componen_cabañas[i].calcular_precio_alojamiento()
                precio = precio - descuento_porcentaje
        
        return precio
                
            