a = [
    [1,2,6],
    [4,2,5],
    [6,5,3]
]

number = int(input("Please enter a number: "))
multiplicación = []

for x,y in enumerate(a):
    multiplicación_fila = []
    for z in range(len(y)):
        multiplicación_fila.append(y[z]*number)
    multiplicación.append(multiplicación_fila)

print("Multiplicación: ", multiplicación)