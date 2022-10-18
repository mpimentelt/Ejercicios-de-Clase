fibonacci = []
x=0
y=1
z=1
fibonacci.append(str(x))
while len(fibonacci)<10:
    fibonacci.append(str(z))
    z = x+y
    x=y
    y=z
print(",".join(fibonacci))