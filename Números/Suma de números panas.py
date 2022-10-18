def son_panas(number1,number2):
    dividers1 = []
    dividers2 = []
    for x in range(1,number1):
        if number1%x==0:
            dividers1.append(x)
    for x in range(1,number2):
        if number2%x==0:
            dividers2.append(x)
    if number1 != number2:
        if sum(dividers1) == number2 and sum(dividers2)==number1:
            return True
        else:
            return False

def suma_de_numeros_panas(panas):
    print(len(panas))

def main(): 
    panas=[]
    number=input("Please enter a number: ")
    while not number.isnumeric():
        number=input("Please enter a number: ")
    else:
        number = int(number)
        for x in range(1,number+1):
            for y in range(1,number+1):
                números_amigos = son_panas(x,y)
                if números_amigos == True:
                    if not x in panas:
                        panas.append(x)
                    if not y in panas:
                        panas.append(y)
        suma_de_numeros_panas(panas)
        
main()