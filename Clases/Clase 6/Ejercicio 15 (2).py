dicc = {}
palabras_input = input("Introduzca la lista de palabras y sus traducciones en el formato palabra:traduccion,palabra:traduccion:\n->")
for par in palabras_input.split(','):
    esp, eng = par.split(':')
    dicc[esp]=eng
frase = input("Introduzca la frase que desea traducir en español:\n->")
for palabra in frase.split():
    if palabra in dicc:
        print (dicc[palabra], end=" ")
    else: 
        print (palabra, end=" ")