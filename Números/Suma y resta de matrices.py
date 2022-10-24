a = [
    [1,2,6],
    [4,2,5],
    [6,5,3]
]
c = [
    [1.3,20,12],
    [1.8,28,15],
    [2,5,40,18]
] 
suma = []
resta = []

for x,y in enumerate(a):
    suma_fila = []
    resta_fila = []
    for z in range(len(y)):
        suma_fila.append(y[z]+c[x][z])
        resta_fila.append(y[z]-c[x][z])
    suma.append(suma_fila)
    resta.append(resta_fila)

print("Suma: ", suma)
print("Resta: ", resta)