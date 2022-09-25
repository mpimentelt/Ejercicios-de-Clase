import random
random_num = str(random.randrange(1,1001))
print (f"Your password is {random_num}")
password = str(input("\nPlease enter the given password: \n->"))

while password != random_num:
    password = str(input("Incorrect password. Please enter the given password: \n->"))
else:
    print("Correct password. You now have access to the program.")