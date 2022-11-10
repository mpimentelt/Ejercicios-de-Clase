from funciones import *

def main():
    print("******** BIENVENIDO A LA BASE DE DATOS DE LOS ESTUDIANTES ********")
    alumnos = []
    while True:
        option = int(input('''
Por favor introduzca una opción válida:
    1. Registrar un estudiante
    2. Ver estudiantes registrados
    3. Ver mejores 5 alumnos
    4. Ver promedio general de los alumnos
    5. Ver cantidad de alumnos por promedio
    6. Salir

->'''))
        if option == 1:
            alumno = registrar_alumno()
            alumno.mostrar()
            alumnos.append(alumno)
        elif option == 2:
            mostrar_db(alumnos)
        elif option == 3:
            ver_top5(alumnos)
        elif option == 4:
            promedio(alumnos)
        elif option == 5:
            clasificar_alumnos_promedio(alumnos)
        elif option == 6:
            break
        else:
            continue   

print("Ha salido exitosamente de la base de datos. Feliz día. ")

main()