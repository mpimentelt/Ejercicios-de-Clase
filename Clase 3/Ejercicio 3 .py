num1 = input ("Please enter the first number: ")
num2 = input ("Please enter the second number: ")
is_valid = True

if num1.isnumeric():
    num1 = float (num1)
else:
    is_valid = False

if num2.isnumeric():
    num2 = float (num2)
else:
    is_valid = False


if is_valid:
    if num2 == 0 :
        print ("Error")
    else:
        print (num1/num2)

else:
    print ("Invalid numbers")