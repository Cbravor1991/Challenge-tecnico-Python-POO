from src.usuario import Usuario

class App:
    def __init__(self , usuarios):
        self.usuarios = usuarios #recibe una lista de usuarios con todo cargado lo pienso para simplificar
        
    def obtener_usuarios_ordenados_por_presupuesto(self):
        usuarios_ordenados = sorted(self.usuarios, key=lambda usuario: usuario.obtener_presupuesto(), reverse=True)
        return usuarios_ordenados
    
    def analizar_producto_segun_presupuesto(self, producto, usuario):
        if (producto.obtener_precio()<= usuario.obtener_presupuesto()):
            print (f"Puede obtener producto")
        else:
            print(f"Su presupuesto no alcanza")
        
        
        
    