number = int(input("Please input a number: "))
acum = 0
if number < 10:
    print(number)
else:
    for i in str(number):
        acum += int(i)
    print(acum)