from selection import selection

def binary_search(lista, number):
    start=0
    final=len(lista)-1
    middle=(start+final)//2
    if len(lista)==1:
        if lista[0]==number:
            return number
        else:
            return -1 #práctica que hay en sistemas cuando algo no se encuentra, o cuando algo no está seleccionado
    if number > lista[middle]:
        return binary_search(lista[middle:final], number)
    elif number < lista[middle]:
        return binary_search(lista[start:middle], number)
    else:
        return lista[middle]


def main():
    lista = [6,5,3,1,8,7,2,4]
    lista = selection(lista)
    number = int(input("Please enter a number: "))
    if binary_search(lista, number) != -1:
        print("The number {} is in the list.".format(number))
    else: 
        print("The number {} is not in the list.".format(number))
main()