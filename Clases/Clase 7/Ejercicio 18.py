a = [[1, 2, 3], [4, 5, 6]]
b = [[-1, 0],[0,1],[1,1]]
lista = []
acum = 0 

for ia in a:
    for j in range(3):
        for k in range(2):
            acum += a[ia][j]*b[j][ia]
        print(acum)