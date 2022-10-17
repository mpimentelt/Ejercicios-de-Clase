number = input("Please enter a number: ")
while not number.isnumeric():
    number = input("Please enter a number: ")
else:
    number = int(number)
    dividers=[]
    prime_numbers=[]
    is_primeproduct = False
    for x in range(1,number):
        if number%x == 0:
            dividers.append(x)
    for x in dividers:
        prime = True
        for i in range(2,x):
            if x%i == 0:
                prime = False
                break
        if prime and x>1:
            prime_numbers.append(x)
    for x in prime_numbers:
        for y in prime_numbers:
            if x*y == number:
                print("The number {} is the product of prime numbers: {} and {}".format(number,x,y))
                is_primeproduct = True
        if is_primeproduct:
            break
    if not is_primeproduct:
        print("Error")