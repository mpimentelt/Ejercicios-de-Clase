n = int(input("Please enter a number:"))
fibonacci = []
x=0
y=1
z=1
fibonacci.append(str(x))
while z <= n:
    fibonacci.append(str(z))
    z = x+y
    x=y
    y=z
print(",".join(fibonacci))