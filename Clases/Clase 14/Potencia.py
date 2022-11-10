def potencia(n,i):
    if i == 0:
        return 1
    return n * (potencia(n,i-1))

def main():
    n = int(input("Enter a number (base)"))
    i = int(input("Enter a number (exponent)"))
    print (potencia(n,i))
main()