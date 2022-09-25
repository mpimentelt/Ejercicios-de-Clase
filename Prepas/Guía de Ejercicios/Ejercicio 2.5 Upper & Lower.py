palabra = input("Introduzca una palabra: ")
is_valid = True

if palabra.isalpha():
    palabra = palabra.lower()
else:
    is_valid = False

if is_valid:
    palabra = palabra.replace("a","A").replace("e","E").replace("i","I").replace("o","O").replace("u","U")
    print(palabra)

else:
    print("Inválido")