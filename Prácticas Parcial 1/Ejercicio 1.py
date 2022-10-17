while True:
    number = input("Please enter a number: ")
    if number.isnumeric():
        number = int(number)
        aux = 0
        aux2 = 0
        for n in range(1,number):
            if number%n==0:
                aux+=n
            else:
                continue
        if not aux == 0:
            for x in range(1,aux):
                if aux%x==0:
                    aux2+=x
                else: 
                    continue
        if aux == aux2:
            print(f"The number {number} is aspiring.")
        else:
            print(f"The number {number} is not aspiring.")
        if input("Would you like to introduce another number? Y-yes or N-no").capitalize() == "N":
            break
        else:
            continue
