edad = input("Indique su edad: ")
while not edad.isnumeric():
    edad = input("Indique una edad válida: ")
else:
    edad = int(edad)
    if edad >= 18:
        print("Si es mayor de edad")
    else: 
        print("No es mayor de edad")