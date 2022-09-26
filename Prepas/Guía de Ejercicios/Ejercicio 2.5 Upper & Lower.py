palabra = input("Introduzca una palabra: ").lower()

if not palabra.isalpha():
    print("Inválido")

else:
    palabra = palabra.replace("a","A").replace("e","E").replace("i","I").replace("o","O").replace("u","U")
    print(palabra)