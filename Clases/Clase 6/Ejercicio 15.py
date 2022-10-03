traductor_dict = {}
traduccion_input = input("Introduzca el diccionario en el formato palabra:traduccion,palabra:traduccion: ")
pares = traduccion_input.split(",")
for palabra_traduccion in pares:
    lista_palabras = palabra_traduccion.split(":")
    key_traduccion = lista_palabras[0]
    value_traduccion = lista_palabras[1]
    traductor_dict[key_traduccion] = value_traduccion