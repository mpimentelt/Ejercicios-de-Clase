number = input("Introduzca un número: ")
while not number.isnumeric():
    number = input("Introduzca un número: ")
else: 
    number = int(number)
    for n in range(1,number+1):
        if number == n*(n+1): 
            print("El número es oblongo")
            break
    else:
        print("El número no es oblongo")