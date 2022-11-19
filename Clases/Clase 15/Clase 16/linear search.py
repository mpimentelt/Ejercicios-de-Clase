def linear_search(lista,number):
    for n in lista:
        if n == number:
            return number

def main():
    lista = [6,5,3,1,8,7,2,4]
    number = int(input("Please enter a number: "))
    if linear_search(lista, number) != None:
        print("The number {} is in the list.".format(number))
    else: 
        print("The number {} is not in the list.".format(number))
main()