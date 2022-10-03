edad = input("Indique su edad: ")
while not edad.isnumeric():
    edad = input("Indique una edad válida: ")
else:
    edad = int(edad)
    if edad < 4:
        precio = 0
    elif edad >= 4 and edad <= 18: 
        precio = 10
    else: 
        precio = 14
print(f"Total a pagar: {precio} $")