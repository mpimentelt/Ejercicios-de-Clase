num1 = input ("Please enter the first number: ")
while not num1.isnumeric():
    num1=input("Invalid number. Please enter the first number: ")

num2 = input ("Please enter the second number: ")
while not num2.isnumeric():
    num2=input("Invalid number. Please enter the second number: ")


else:
    num1 = float (num1)
    num2 = float (num2)
    if num2 == 0 :
        print ("Error")
    else:
        print (num1/num2)