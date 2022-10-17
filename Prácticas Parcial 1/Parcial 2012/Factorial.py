number = input("Please enter a number: ")
while not number.isnumeric():
    number = input("Please enter a number: ")
else:
    number = int(number)
    aux = 1
    for x in range(1,number+1):
        aux *= x
    print("El factorial de {} es: {}".format(number, aux))