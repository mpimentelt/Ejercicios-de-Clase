def fibonacci(max, num1=0, num2=1):
    print(num1, end=" ")
    if num2>max:
        return num1
    return fibonacci(max, num2, num1+num2)


def main():
    max = int(input("Please enter a number: "))
    fibonacci(max)

main()