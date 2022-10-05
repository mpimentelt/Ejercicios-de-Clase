acum = 0
while True: 
    edad = input("Indique la edad de la persona para la que comprará la entrada: ")
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
            acum += precio
    if input("¿Desea comprar otra entrada? Marque 1 para si y 2 para no") == "2":
        break

print(f"Total a pagar: {acum} $")