number = input("Please enter a number: ")
is_valid = True
cont = 0

if number.isnumeric:
    number = int (number)
else:
    is_valid = False

if is_valid:
    aux = number - 1
    if number <= 1:
        print (f"The number {number} is not prime.")
    else:
        while aux > 1:
            if number % aux == 0:
                cont += 1
            aux -= 1
        if cont == 0:
            print (f"The number {number} is prime.")
        else:
            print (f"The number {number} is not prime.")

else: 
    print ("Invalid numbers")