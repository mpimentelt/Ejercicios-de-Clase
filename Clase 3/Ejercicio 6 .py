option = int(input("Please enter a valid option: \n1. Vegetarian \n2. Non-vegetarian \n->"))

if int (option) == 1:
    ingredient = int (input("Please enter the ingredient you want: \n1. Bell pepper \n2. Tofu \n->"))
    if int (ingredient) == 1:
        ingredient = "bell pepper"
    elif int (ingredient) == 2:
        ingredient = "tofu"
    else:
        print("Invalid option")
    print  (f"The pizza is vegetarian and the ingredients are: tomato, mozzarella and {ingredient}")
    
elif int (option) == 2:
    ingredient = int (input("Please enter the ingredient you want: \n1. Pepperoni \n2. Salmon \n3. Jam \n->"))
    if int (ingredient) == 1:
        ingredient = "pepperoni"
    elif int (ingredient) == 2:
        ingredient = "salmon"
    elif int (ingredient) == 3:
        ingredient = "jam"
    else: 
        print("Invalid option")
    print  (f"The pizza is vegetarian and the ingredients are: tomato, mozzarella and {ingredient}")

else:
    print("Invalid option")
