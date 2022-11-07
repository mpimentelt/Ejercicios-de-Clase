class Redactor:
    def __init__(self, nombre, id, seccion):
        self.nombre = nombre
        self.id = id
        self.seccion = seccion

class Jefe(Redactor):
    def __init__(self, nombre, id, seccion, list_redactores):
        super().__init__(nombre, id, seccion)
        self.cargo = "Jefe"
        self.redactores = list_redactores

class Articulo:
    def __init__(self, titulo, resumen, cuerpo, imagenes, publicacion, creacion, redactor):
        self.titulo = titulo
        self.resumen = resumen
        self.cuerpo = cuerpo
        self.imagenes = imagenes
        self.publicacion = publicacion
        self.creacion = creacion
        self.redactor = redactor
    
class AnuncioComercial:
    def __init__(self, nombre, cedula, seccion, titulo, cuerpo):
        self.nombre = nombre
        self.cedula = cedula
        self.seccion = seccion
        self.titulo = titulo
        self.cuerpo = cuerpo

class AnuncioClasificado:
    def __init__(self, precio, publicacion, dias, tipo_articulo):
        self.precio = precio
        self.publicacion = publicacion
        self.dias = dias
        self.tipo_articulo = tipo_articulo

class Vehiculo(AnuncioClasificado):
    def __init__(self, precio, publicacion, dias, tipo_articulo, marca, modelo, año, kilometraje):
        super().__init__(precio, publicacion, dias, tipo_articulo)
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

class Vivienda(AnuncioClasificado):
    def __init__(self, precio, publicacion, dias, tipo_articulo, metros, cuartos, baños, estacionamiento, ley):
        super().__init__(precio, publicacion, dias, tipo_articulo)
        self.metros = metros
        self.cuartos = cuartos
        self.baños = baños
        self.estacionamiento = estacionamiento
        self.ley = ley