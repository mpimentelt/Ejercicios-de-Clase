print (""" Operaciones disponibles:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. Módulo
7. Comparar mayor o menor que
8. Valor absoluto """)

operacion_mat = int(input("Indique el número de la operación matemática que desee hacer: "))

if int (operacion_mat) == 1 :
    num1 = float (input ("Indique el primer número que desea utilizar"))
    num2 = float (input ("Indique el segundo número que desea utilizar"))
    resultado = num1 + num2
    print (f"{resultado}")
    
if int (operacion_mat) == 2 :
    num1 = float (input ("Indique el primer número que desea utilizar"))
    num2 = float (input ("Indique el segundo número que desea utilizar"))
    resultado = num1 - num2
    print (f"{resultado}")

if int (operacion_mat) == 3 :
    num1 = float (input ("Indique el primer número que desea utilizar"))
    num2 = float (input ("Indique el segundo número que desea utilizar"))
    resultado = num1 * num2
    print (f"{resultado}")

if int (operacion_mat) == 4 :
    num1 = float (input ("Indique el primer número que desea utilizar"))
    num2 = float (input ("Indique el segundo número que desea utilizar"))
    resultado = num1 / num2
    print (f"{resultado}")

if int (operacion_mat) == 5 :
    num1 = float (input ("Indique el primer número que desea utilizar"))
    num2 = float (input ("Indique el segundo número que desea utilizar"))
    resultado = num1 ** num2
    print (f"{resultado}")

if int (operacion_mat) == 6 :
    num1 = float (input ("Indique el primer número que desea utilizar"))
    num2 = float (input ("Indique el segundo número que desea utilizar"))
    resultado = num1 % num2
    print (f"{resultado}")

if int (operacion_mat) == 7 :
    num1 = float (input ("Indique el primer número que desea utilizar"))
    num2 = float (input ("Indique el segundo número que desea utilizar"))
    resultado = num1 - num2
    print (f"{resultado}")

if int (operacion_mat) == 8 :
    num = float (input ("Indique el número que desea utilizar"))
    resultado = abs(num)
    print (f"{resultado}")