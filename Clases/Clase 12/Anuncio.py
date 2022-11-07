class AnuncioComercial:
    def __init__(self, imagen, seccion):
        self.imagen = imagen
        self.seccion = seccion

class AnuncioClasificado:
    def __init__(self, precio, publicacion, dias, tipo_articulo):
        self.precio = precio
        self.publicacion = publicacion
        self.dias = dias
        self.tipo_articulo = tipo_articulo

class AnuncioClasificadoVehiculo(AnuncioClasificado):
    def __init__(self, precio, publicacion, dias, marca, modelo, año, color, km):
        super().__init__(precio, publicacion, dias, "Vehículo")
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.kilometraje = km

class AnuncioClasificadoVivienda(AnuncioClasificado):
    def __init__(self, precio, publicacion, dias, metros, cuartos, baños, estacionamiento, ley):
        super().__init__(precio, publicacion, dias, "Vivienda")
        self.metros = metros
        self.cuartos = cuartos
        self.baños = baños
        self.puestos_estacionamiento = estacionamiento
        self.aplica_ley = ley

