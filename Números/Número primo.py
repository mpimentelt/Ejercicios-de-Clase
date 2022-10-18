number = input("Introduzca un número: ")
while not number.isnumeric():
    number = input("Introduzca un número: ")
else: 
    number = int(number)
    prime = True
    for x in range(2,number):
        if number%x == 0:
            prime = False
            break
    if prime and number>1:
        print("El número {} es primo.".format(number))
    else: 
        print("El número {} no es primo.".format(number))