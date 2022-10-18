def get_number():
    number = input("Introduzca un número: ")
    while not number.isnumeric():
        number = input("Introduzca un número: ")
    else: 
        return int(number)

def is_primo(number):
    prime = True
    for x in range(2,number):
        if number%x == 0:
            prime = False
    if prime and number>1:
        return True
    else: 
        return False

def is_compuesto(number):
    compuesto = False
    for x in range(2,number):
        if number%x == 0:
            compuesto = True
    if compuesto and number>1:
        return True
    else:
        return False

def is_oblongo(number):
    for n in range(1,number+1):
        if number == n*(n+1): 
            return True
    else:
        return False

def is_palíndromo(number):
    number = str(number)
    if len(number) >1:
        if number == number[::-1]:
            return True
    else:
        return False

def is_perfecto(number):
    acum = 0
    for x in range(1,number):
        if number%x == 0:
            acum += x
    if acum == number:
        return True
    else: 
        return False

def is_abundante(number):
    acum = 0
    for x in range(1,number):
        if number%x == 0:
            acum += x
    if acum > number:
        return True
    else: 
        return False

def is_deficiente(number):
    acum = 0
    for x in range(1,number):
        if number%x == 0:
            acum += x
    if acum < number:
        return True
    else: 
        return False

def is_cuadrado(number):
    for x in range(1,number+1):
        if x**2 == number:
            return True
    else:
        return False

def is_libre_de_cuadrados(number):
    for x in range(1,number+1):
        if x**2 == number:
            return False
    else:
        return True

def main():
    number = get_number()
    if is_primo(number):
        print("El número {} es primo.".format(number))
    if is_compuesto(number): 
        print("El número {} es compuesto.".format(number))
    if is_oblongo(number): 
        print("El número {} es oblongo.".format(number))
    if is_palíndromo(number): 
        print("El número {} es palíndromo.".format(number))
    if is_perfecto(number): 
        print("El número {} es perfecto.".format(number))
    if is_abundante(number): 
        print("El número {} es abundante.".format(number))
    if is_deficiente(number): 
        print("El número {} es deficiente.".format(number))
    if is_cuadrado(number): 
        print("El número {} es cuadrado.".format(number))
    if is_libre_de_cuadrados(number):
        print("El número {} es libre de cuadrados.".format(number)) 

main()