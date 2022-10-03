compra = {}
total = 0
while True: 
    item = input("¿Qué artículo desea comprar?")
    precio = float (input("¿Cuál es el precio de ese artículo?"))
    compra[item]=precio
    if input("¿Desea agregar más artículos a su compra? Marcar 1 para si y 2 para no") == "2":
        print("Lista de compra:\nArtículo\tPrecio\n")
        for item, precio in compra.items(): 
            print("{:<15} {}$".format(item, precio))
            total += precio
        print ("\nTotal:\t\t{}$".format(total))
        break