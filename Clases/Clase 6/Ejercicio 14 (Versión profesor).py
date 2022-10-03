personal_data = {}
while True:
    key = input("What data would you like to enter? Eg: name, age, gender, etc")
    value = input("Please enter the data value")
    personal_data[key]=value
    for key, value in personal_data.items():
        print(f"Your {key} is {value}")
    if input("Do you want to continue adding data?\nY-Yes\nN-No") == "N":
        break