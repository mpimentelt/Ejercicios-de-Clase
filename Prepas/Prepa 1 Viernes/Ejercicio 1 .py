for number in range(0,31):
    if number == 0:
        print(number)
    elif number%3 == 0 and number%5 == 0:
        print("unimet")
    elif number%3 == 0:
        print("uni")
    elif number%5 == 0: 
        print("met")
    else: 
        print (number)