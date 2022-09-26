number = input("Please enter a number: ")
while not number.isnumeric():
    number = input("Error. Please enter a number: ")
else:
    number = int(number)
    for i in range(1,number+1):
        print (i*"*")
