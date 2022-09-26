number = input("Please enter a number: ")
while not number.isnumeric():
    number = input("Error. Please enter a number: ")
else:
    number = int(number)
    for i in range(1,number+1,2): #arreglar el tema de la altura
        aux = i
        while aux >= 1:
            if aux == 1:
                print (aux)
            else:
                print (aux, end=" ")
            aux -= 2