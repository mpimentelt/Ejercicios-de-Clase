number1=input("Please enter a number: ")
while not number1.isnumeric():
    number1=input("Please enter a number: ")
else:
    number1=int(number1)
number2=input("Please enter a number: ")
while not number2.isnumeric():
    number2=input("Please enter a number: ")
else:
    number2=int(number2)
dividers1 = []
dividers2 = []
for x in range(1,number1):
    if number1%x==0:
        dividers1.append(x)
for x in range(1,number2):
    if number2%x==0:
        dividers2.append(x)
if sum(dividers1) == number2 and sum(dividers2)==number1:
    print("Los números {} y {} son amigos.".format(number1,number2))
else:
    print("Los números {} y {} no son amigos.".format(number1,number2))