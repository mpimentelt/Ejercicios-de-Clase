number = input("Introduzca un número: ")
isvalid = False
acum = 0
while not number.isnumeric():
    number = input("Introduzca un número: ")
else: 
    number = int(number)
    for i in str(number):
        repeticiones = str(number).count(i)
        if repeticiones == len(str(number)):
            i = int (i)
            acum += i
        else:
            break
    for n in range(0,acum+1):
        if n**2 == acum:
            isvalid = True
if isvalid: 
    print("El número {} es repunit y la suma de sus dígitos {} es un número cuadrado".format(number,acum))
else:
    print("El número {} no es repunit y la suma de sus dígitos no es un número cuadrado".format(number))