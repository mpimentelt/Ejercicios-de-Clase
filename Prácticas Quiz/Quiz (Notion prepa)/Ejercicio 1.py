number = input("Please enter a number: ")
iscurious = False
while not number.isnumeric:
    number = input("Please enter a number: ")
else:
    number = int(number)
    n = number**(1/2)
    for i in str(number):
        i = int(i)
        if i == n:
            iscurious = True
            break
if iscurious:
    print("The number {} is curious".format(number))
else: 
    print("The number {} is not curious".format(number))