x = str(input("Introduzca una palabra o número entero: \n->")).lower()
lista = x.split("")
reverse_lista = lista.reverse()
if lista == reverse_lista:
    print(f"{x} es un palíndromo.")
else: 
    print(f"{x} no es un palíndromo.")
if x == x[::-1]:
    print(f"{x} es un palíndromo.")
else: 
    print(f"{x} no es un palíndromo.")