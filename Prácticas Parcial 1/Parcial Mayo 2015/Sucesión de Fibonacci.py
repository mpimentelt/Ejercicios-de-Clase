number = int(input("Please enter a number:"))
fibonacci = []
x=0
y=1
z=1
fibonacci.append(str(x))
while z <= number:
    fibonacci.append(z)
    z = x+y
    x=y
    y=z
if number in fibonacci: 
    print("El número {} pertenece a la sucesión de fibonacci".format(number))
else:
    print("El número {} no pertenece a la sucesión de fibonacci".format(number))