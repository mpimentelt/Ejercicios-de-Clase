isvalid = False
día = input("Indique un día: ")
mes = input("Indique un mes (en números): ")
año = input("Indique un año: ")

meses = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio", 7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}

if año.isnumeric():
    if int(año)%4 == 0:
        if mes.isnumeric and int(mes) in range(1,13):
            if int(mes) == 2:
                if día.isnumeric() and int(día) in range(1,30):
                    isvalid = True
            if int(mes) == [1, 3, 5, 7, 8, 10, 12]:
                if día.isnumeric() and int(día) in range(1,32):
                    isvalid = True
            else: 
                if día.isnumeric() and int(día) in range(1,31):
                    isvalid = True
    else:
        if mes.isnumeric and int(mes) in range(1,13):
            if int(mes) == 2:
                if día.isnumeric() and int(día) in range(1,29):
                    isvalid = True
            if int(mes) == [1, 3, 5, 7, 8, 10, 12]:
                if día.isnumeric() and int(día) in range(1,32):
                    isvalid = True
            else: 
                if día.isnumeric() and int(día) in range(1,31):
                    isvalid = True

if isvalid:
    print("Fecha: {} de {} de {}".format(int(día),meses[int(mes)],int(año)))

else:
    print("Fecha inválida")