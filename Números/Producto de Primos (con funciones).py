def get_number():
    number = input("Please enter a number: ")
    while not number.isnumeric():
        number = input("Please enter a number: ")
    else:
        number = int(number)
        return number

def get_dividers(number):
    dividers=[]
    for x in range(1,number):
        if number%x == 0:
            dividers.append(x)
    return dividers

def get_prime(list):
    prime_numbers=[]
    for x in list:
        prime = True
        for i in range(2,x):
            if x%i == 0:
                prime = False
                break
        if prime and x>1:
            prime_numbers.append(x)
    return prime_numbers

def get_product(numbers, number):
    is_primeproduct = False
    for x in numbers:
        for y in numbers:
            if x*y == number:
                print("The number {} is the product of prime numbers: {} and {}".format(number,x,y))
                is_primeproduct = True
        if is_primeproduct:
            break
    if not is_primeproduct:
        print("Error")

def main ():
    number = get_number()
    dividers = get_dividers(number)
    prime_dividers = get_prime(dividers)
    product = get_product(prime_dividers, number)

main()