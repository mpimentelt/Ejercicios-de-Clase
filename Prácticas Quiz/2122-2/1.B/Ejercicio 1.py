number = input("Introduzca un número: ")
isvalid = False
aux = 0
while not number.isnumeric():
    number = input("Introduzca un número: ")
else: 
    number = int(number)
    if number%2 == 0:
        for n in range(1,number+1):
            aux += n-1
            if aux == number:
                isvalid = True
                break

if isvalid:
    print(f"El número {number} es par y triangular.")
else:
    print(f"El número {number} no es par y triangular.")