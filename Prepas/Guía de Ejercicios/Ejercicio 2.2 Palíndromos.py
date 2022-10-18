x = str(input("Introduzca una palabra o número entero: \n->")).lower()
if x == x[::-1]:
    print(f"{x} es un palíndromo.")
else: 
    print(f"{x} no es un palíndromo.")