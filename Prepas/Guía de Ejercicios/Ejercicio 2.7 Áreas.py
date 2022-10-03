import math
figura = input("Introduzca el número de la figura cuya área desee calcular:\n1. Circunferencia\n2. Elipse\n3. Cuadrado\n4. Rectángulo\n5. Triángulo\n6. Rombo\n->")
while not figura.isnumeric():
    figura = input("Por favor introduzca una opción válida:\n1. Circunferencia\n2. Elipse\n3. Cuadrado\n4. Rectángulo\n5. Triángulo\n6. Rombo\n->")    
else:
    figura = int(figura)
while not figura in range(1,7):
    figura = input("Por favor introduzca una opción válida: 1. Circunferencia\n2. Elipse\n3. Cuadrado\n4. Rectángulo\n5. Triángulo\n6. Rombo\n->")
else:
    if figura == 1:
        r = input("Introduzca el valor del radio de la circunferencia: ")
        while not r.isnumeric():
            r = input("Introduzca el valor del radio de la circunferencia: ")
        else:
            r = float(r)
            print(f"El área de una circunferencia de radio {r} es {math.pi * r**2}")
    if figura == 2:
        a = input("Introduzca el valor del semieje horizontal de la elipse: ")
        while not a.isnumeric():
            a = input("Introduzca el valor del semieje horizontal de la elipse: ")
        else:
            a = float(a)
        b = input("Introduzca el valor del semieje vertical de la elipse: ")
        while not b.isnumeric():
            b = input("Introduzca el valor del semieje vertical de la elipse: ")
        else:
            b = float(b)
        print(f"El área de la elipse de semieje horizontal {a} y semieje horizontal {b} es {math.pi*a*b}")
    if figura == 3:
        l = input("Introduzca el valor del lado del cuadrado: ")
        while not l.isnumeric:
            l = input("Introduzca el valor del lado del cuadrado: ")
        else: 
            l = float(l)
        print(f"El área del cuadrado de lado {l} es {l**2}")
    if figura == 4:
        b = input("Introduzca el valor de la base del rectángulo: ")
        while not b.isnumeric:
             b = input("Introduzca el valor de la base del rectángulo: ")
        else: 
            b = float(b)
        h = input("Introduzca el valor de la altura del rectángulo: ")
        while not h.isnumeric:
             h = input("Introduzca el valor de la altura del rectángulo: ")
        else: 
            h = float(h)
        print (f"El área del rectángulo de base {b} y de altura {h} es {b*h}")
    if figura == 5: 
        b = input("Introduzca el valor de la base del triángulo: ")
        while not b.isnumeric:
             b = input("Introduzca el valor de la base del triángulo: ")
        else: 
            b = float(b)
        h = input("Introduzca el valor de la altura del triángulo: ")
        while not h.isnumeric:
             h = input("Introduzca el valor de la altura del triángulo: ")
        else: 
            h = float(h)
        print (f"El área del triángulo de base {b} y de altura {h} es {(b*h)/2}")
    if figura == 6: 
        dm = input("Introduzca el valor de la diagonal menor del rombo: ")
        while not dm.isnumeric():
            dm = input("Introduzca el valor de la diagonal menor del rombo: ")
        else:
            dm = float(dm)
        dM = input("Introduzca el valor de la diagonal mayor del rombo: ")
        while not dM.isnumeric():
            dM = input("Introduzca el valor de la diagonal mayor del rombo: ")
        else:
            dM = float(dM)
        print (f"El área del rombo de diagonal menor {dm} y diagonal mayor {dM} es {(dm*dM)/2}")