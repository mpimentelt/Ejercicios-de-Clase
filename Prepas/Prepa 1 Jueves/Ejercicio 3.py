x = "Bienvenidos a la prepa de algoritmosa"
count = 0
for letter in x:
    if letter == "a" and len(x) > count+1:
        if x[count+1] == "l":
            print (f"Hay un al en la posición {count}-{count+1}")
    count += 1