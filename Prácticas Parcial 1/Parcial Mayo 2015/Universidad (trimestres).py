def main():
    aspirantes=0
    alumnos1=0
    alumnos2=0
    acum_promedios = 0
    acum_promedios1 = 0
    acum_promedios2 = 0
    while True: 
        aspirante = {
            "cédula": input("Por favor indique su cédula: "),
            "promedio": input("Por favor indique su promedio: ")
        }
        while not aspirante["promedio"].isnumeric() and int(aspirante["promedio"])>20:
            aspirante["promedio"] = input("Por favor indique su promedio: ")
        else:
            aspirante["promedio"] = int(aspirante["promedio"])
            aspirantes+=1
            print("****** ASPIRANTE ******")
            print("C.I.: ", aspirante["cédula"])
            print("Promedio: ", aspirante["promedio"])
            if aspirante["promedio"] >= 18:
                print("Trimestre asignado: 2")
                alumnos2+=1
            elif aspirante["promedio"] >= 12:
                print("Trimestre asignado: 1")
                alumnos1+=1
            else:
                print("Rechazado")
main()