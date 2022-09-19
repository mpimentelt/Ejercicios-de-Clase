number = input ("Please enter a number")

if number.isnumeric():
    number = int (number)
else:
    is_valid = False

if is_valid: 
    if number%2==0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")