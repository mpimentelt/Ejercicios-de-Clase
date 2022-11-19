def partition(lista):
    menores = []
    mayores = []
    pivote = lista[0]
    for i in range(len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        elif lista[i] > pivote:
            mayores.append(lista[i])
    
    return menores, pivote, mayores

def quick_sort(lista):
    if len(lista)<2:
        return lista
    menor,pivote,mayor = partition(lista)
    print(menor,pivote,mayor)
    return quick_sort(menor) + [pivote] + quick_sort(mayor)

def main():
    lista = [6,5,3,1,8,7,2,4]
    print(lista)
    lista2 = quick_sort(lista)
    print(lista2)
main()