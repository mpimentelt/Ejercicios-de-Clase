from alumno import Alumno

def registrar_alumno():
    print("Introduzca los siguientes parámetros: ")
    nombre = input("Nombre completo: ")
    grado = input("Grado que cursa: ")
    promedio = input("Promedio: ")
    while not promedio.isnumeric():
        promedio = input("Promedio: ")
    else:
        promedio = int(promedio)
    direccion = input("Dirección en la que reside: ")
    nombre_representante = input("Nombre del representante: ")
    telf_representante = input("Teléfono del representante: ")
    becado = False
    if promedio >= 18: 
        becado = True
    return Alumno(nombre,grado,promedio,direccion,nombre_representante,telf_representante,becado)

def mostrar_db(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados.")
    else: 
        for index, alumno in enumerate(alumnos):
            print(index+1)
            print("---------------------------------------")
            alumno.mostrar()
            print("=======================================")

def ver_top5(alumnos):
    alumnos.sort(key=lambda alumno: alumno.promedio, reverse=True)
    for index, alumno in alumnos:
        if index < 5:
            print(index+1)
            print("---------------------------------------")
            alumno.mostrar()
            print("=======================================")

def promedio(alumnos):
    promedios=[]
    for alumno in alumnos:
        promedios.append(alumno.promedio)
    print(f"El promedio general del colegio es de {sum(promedios)/len(promedios)} puntos.")

def clasificar_alumnos_promedio(alumnos):
    menores10 = 0
    entre10y16 = 0
    entre16y20 = 0
    for alumno in alumnos:
        if alumno.promedio < 10:
            menores10+=1
        if alumno.promedio >= 10 and alumno.promedio < 16:
            entre10y16 += 1
        else:
            entre16y20 += 1
    print(f'''Promedios:
Menores a 10: {menores10} alumnos
Entre 10 y 15.9: {entre10y16} alumnos
Entre 16 y 20: {entre16y20} alumnos
''')
