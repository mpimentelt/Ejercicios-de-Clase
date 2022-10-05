number = int(input("Indique un número entre 2 y 12:"))
combinaciones = []
for x in range(1,7):
    for y in range(1,7):
        if x+y==number:
            if sorted([x,y]) in combinaciones:
                continue
            else: 
                combinaciones.append([x,y])

print(f"Combinaciones para {number}:")
for combinacion in combinaciones:
    print("\t*{}-{}".format(combinacion[0],combinacion[1]))