#parte 1
valores_x = [2,5,9,13]
tabla_valores = []
for x in valores_x:
    par_ordenado = (x,2**x)
    tabla_valores.append(par_ordenado)
print(tabla_valores)

#parte 2
coord2 = [(4,1),(25,11),(8,5),(16,8),(45,77),(10,10),(4,1),(34,2),(25,11),(8,5)]
print("\nx\ty")
print("---------")
for par in coord2:
    if coord2.count(par)>1:
        coord2.remove(par)
coord2 = list(set(coord2))
coord2.sort()
for coord in coord2:
    print("{}\t{}".format(coord[0],coord[1]))