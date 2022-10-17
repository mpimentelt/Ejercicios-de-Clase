vectorA = [1,2,3]
vectorB = [-1,0,2]
acum_total = 0

for index in range(len(vectorA)):
    acum_total += (vectorA[index]*vectorB[index])

print(f"Result: {acum_total}")