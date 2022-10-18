number = input("Por favor introduzca un número entero positivo: ")
while not number.isnumeric():
    number = input("Inválido. Por favor introduzca un número entero positivo: ")
else:
    number = int (number)
    for i in range(1,number+1): 
        if i%2 != 0:
            if i+2 >= number: 
                print (i)
            else:
                print(i, end=",")
        