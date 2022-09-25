print (""" Operaciones disponibles:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. Módulo
7. Comparar mayor o menor que
8. Valor absoluto """)

operacion_mat = input("Indique el número de la operación matemática que desee hacer: ")
is_valid = True

if operacion_mat.isnumeric():
    operacion_mat = int (operacion_mat)
else:
    is_valid = False

if is_valid:
    if int (operacion_mat) in range (1,8):
        num1 = input ("Indique el primer número que desea utilizar")
        num2 = input ("Indique el segundo número que desea utilizar")
        if num1.isnumeric():
            num1 = float (num1)
        else:
            is_valid = False
        if num2.isnumeric():
            num2 = float (num2)
        else:
            is_valid = False
        if is_valid: 
            if int (operacion_mat) == 1:
                print(f"{num1}+{num2}={num1+num2}")
            elif int (operacion_mat) == 2:
                print(f"{num1}-{num2}={num1-num2}")
            elif int (operacion_mat) == 3:
                print(f"{num1}*{num2}={num1*num2}")
            elif int (operacion_mat) == 4 :
                if num2 == 0:
                    print ("Error")
                else:
                    print(f"{num1}/{num2}={num1/num2}")
            elif int (operacion_mat) == 5 :
                print(f"{num1}**{num2}={num1**num2}")
            elif int (operacion_mat) == 6 :
                if num2 == 0:
                    print ("Error")
                else:
                    print(f"{num1}%{num2}={num1%num2}")
            else:
                if num1>num2:
                    print(f"{num1}>{num2}")
                elif num1<num2:
                    print(f"{num1}<{num2}")
                else:
                    print(f"{num1}={num2}")
        else: 
            print("Error")
    elif int (operacion_mat) == 8:
        num = (input ("Indique el número que desea utilizar"))
        if num.isnumeric():
            num = float (num)
        else:
            is_valid = False
        if is_valid:
            print(f"|{num}|={abs(num)}")
        else: 
            print("Error")

else:
    print ("El valor ingresado no corresponde a ninguna operación")