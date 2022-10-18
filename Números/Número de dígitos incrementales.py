while True:
    number = input("Por favor ingrese un número: ")
    digits = []
    if number.isnumeric():
        number = int(number)
        if number in range(100,1000):
            number = str(number)
            for x in number:
                digits.append(x)
            if digits[0]<digits[1] and digits[1]<digits[2]:
                print("SI")
            else:
                print("NO")
        else:
            print("Ingreso inválido. Por favor vuelva a intentarlo")
    else:
        print("Ingreso inválido. Por favor vuelva a intentarlo")