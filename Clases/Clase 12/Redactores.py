class Redactor:
    def __init__(self, nombre, ci):
        self.nombre = nombre
        self.cedula = ci
    
    def escribir_articulo(self):
        print("Estoy escribiendo un artículo")
    
class JefeRedactor(Redactor):
    def __init__(self, nombre, ci, seccion, redactores):
        super().__init__(nombre, ci, seccion)
        grupo_redactores = redactores
    
    def supervisar(self):
        print("Todo bien")
    
    def decidir(self, articulo):
        print("Artículo aprobado: ", articulo)
