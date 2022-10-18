def main():
    aspirantes=0
    alumnos1=0
    alumnos2=0
    acum_promedios = 0
    acum_promedios1 = 0
    acum_promedios2 = 0
    print("******* BIENVENIDO *******")
    while True:
        aspirante = {
            "cédula": input("Por favor indique su cédula: "),
            "promedio": input("Por favor indique su promedio: ")
        }
        if aspirante["promedio"].isnumeric() and int(aspirante["promedio"]) in range(1,21):
            aspirante["promedio"] = int(aspirante["promedio"])
            aspirantes+=1
            acum_promedios += aspirante["promedio"]
            print("****** ASPIRANTE ******")
            print("C.I.: ", aspirante["cédula"])
            print("Promedio: ", aspirante["promedio"])
            if aspirante["promedio"] >= 18:
                print("Trimestre asignado: 2")
                alumnos2+=1
                acum_promedios2 += aspirante["promedio"]
            elif aspirante["promedio"] >= 12:
                print("Trimestre asignado: 1")
                alumnos1+=1
                acum_promedios1 += aspirante["promedio"]
            else:
                print("Rechazado")
        else:
            print("El valor ingresado para el promedio no es válido. Por favor vuelva a intentarlo.")
            continue
        if input("¿Desea agregar otro aspirante? S-si o N-no\n->").capitalize() == "N":
            break
    print("******* ESTADÍSTICAS DE LOS ASPIRANTES *******")
    print("Cantidad de aspirantes: ", aspirantes)
    print("Cantidad de alumnos asignados al trimestre 1: ", alumnos1)
    print("Cantidad de alumnos asignados al trimestre 2: ", alumnos2)
    if not aspirantes == 0:
        print("Promedio General de los aspirantes: ", acum_promedios/aspirantes)
    else:
        print("Promedio General de los aspirantes: no hay aspirantes")
    if not alumnos1==0:
        print("Promedio General de los aspirante asignados al trimestre 1: ", acum_promedios1/alumnos1)
    else:
        print("Promedio General de los aspirantes: no hay aspirantes asignados al trimestre 1")
    if not alumnos2==0:
        print("Promedio General de los aspirante asignados al trimestre 2: ", acum_promedios2/alumnos2)
    else:
        print("Promedio General de los aspirantes: no hay aspirantes asignados al trimestre 2")

main()