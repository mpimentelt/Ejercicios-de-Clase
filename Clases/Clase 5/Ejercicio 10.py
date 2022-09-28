number = input("Please enter a number: ")
while not number.isnumeric():
    number = input("Error. Please enter a number: ")
else:
    number = int(number)
    number += number-1
    for i in range(1,number+1,2):
        aux = i
        while aux >= 1:
            if aux == 1:
                print (aux)
            else:
                print (aux, end=" ")
            aux -= 2