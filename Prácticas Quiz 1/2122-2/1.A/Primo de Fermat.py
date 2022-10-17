number = input("Introduzca un número: ")
while not number.isnumeric():
    number = input("Introduzca un número: ")
else: 
    number = int(number)
    for aux in range(1,number+1):
        if ((2**2)**aux)+1 == number:
            print("El número {} es primo de Fermat".format(number))
            break
    else: 
        print("El número {} es no primo de Fermat".format(number))