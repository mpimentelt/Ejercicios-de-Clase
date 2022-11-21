def main():
    lista = [6,5,3,1,8,7,2,4] #1
    print(lista) #1
    for i in range(len(lista)): #n
        temp = i #n
        valor = lista[i] #n
        j = i-1 #n
        while j>=0 and valor<lista[j]: #n**2
            lista[temp] = lista[j] #n**2
            lista[j] = valor #n**2
            temp -= 1 #n**2
            j -= 1 #n**2
    print(lista) #1
main()

#5n**2 + 4n + 2 = 0n**2