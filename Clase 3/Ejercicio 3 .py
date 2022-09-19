num1 = input ("Indique el primer número")
num2 = input ("Indique el segundo número")

if num1.isnumeric():
    num1 = float (num1)
else:
    is_valid = False

if num2.isnumeric():
    num2 = float (num2)
else:
    is_valid = False


if is_valid:
    if (num2) == 0 :
        print ("Error")
    else:
        resultado = num1 / num2
        print (f"{resultado}")

else:
    print ("Invalid numbers")