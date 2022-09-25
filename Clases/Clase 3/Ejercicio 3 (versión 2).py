num1 = input ("Please enter the first number: ")
num2 = input ("Please enter the second number: ")

if not num1.isnumeric():
    print ("Invalid numbers")

elif not num2.isnumeric():
   print ("Invalid numbers")

else:
    if num2 == 0 :
        print ("Error")
    else:
        print (num1/num2)