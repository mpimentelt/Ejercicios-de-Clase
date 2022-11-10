class Alumno():
    def __init__(self, nombre, grado, promedio, direccion, nombre_representante, telf_representante, becado) -> None:
        self.nombre = nombre
        self.grado = grado
        self.promedio = promedio
        self.direccion = direccion
        self.nombre_representante = nombre_representante
        self.telf_representante = telf_representante
        self.becado = becado
    
    def mostrar(self):
        print(f'''Nombre: {self.nombre}
Grado: {self.grado}
Promedio: {self.promedio}
Dirección: {self.direccion}
Nombre del Representante: {self.nombre_representante}
Teléfono del Representante: {self.telf_representante}
Becado: {self.becado}
        ''')
    
    def mostrar_top5(self):
        print(f'''Nombre: {self.nombre}
Grado: {self.grado}
Promedio: {self.promedio}
        ''')