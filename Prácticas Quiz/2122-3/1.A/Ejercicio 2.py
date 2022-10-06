infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db=[]
while True: 
    menu = input("Please enter a valid option\n1. Register an infractor\n2. Eliminate an infractor\n3. Show registered fees\n4. Exit")
    while not menu.isnumeric():
        continue
    else:
        menu = int(menu)
    if menu == 1:
        infractor={}
        infractor["name"] = input("Please enter the infractor's name: ")
        infractor["last_name"] = input("Please enter the infractor's last name: ")
        infractor["id_card"] = input("Please enter the infractor's idcard: ")
        while not infractor["id_card"].isnumeric():
            infractor["id_card"] = input("Please enter the infractor's idcard: ")
        else:
            infractor["id_card"] = int(infractor["id_card"])
        infractor["infraction_id"] = input("Please enter the infraction id: ")
        while not infractor["infraction_id"].isnumeric():
            infractor["infraction_id"] = input("Please enter the infractor's idcard: ")
        else:
            infractor["infraction_id"] = int(infractor["infraction_id"])
            for key,value in infraction.items():
                if infractor["infraction_id"]==key:
                    infractor["infraction_id"]=value
        infractor["officer"] = input("Please enter a valid option for the officer:\n1. Luis Bello\n2. Jose Quevedo\n3. Antonio Guerra")
        while not infractor["officer"].isnumeric():
            infractor["officer"] = input("Please enter the infractor's idcard: ")
        else:
            infractor["officer"] = int(infractor["officer"])
            for key,value in officers.items():
                if infractor["officer"]==key:
                    infractor["officer"]=value
        db.append(infractor)
    elif menu == 2:
        infractor_id = input("Please enter the infractor's idcard: ")
        while not infractor_id.isnumeric():
            infractor_id = input("Please enter the infractor's idcard: ")
        else:
            infractor_id = int(infractor_id)
            for infractor in db:
                if infractor_id == infractor["id_card"]:
                    for key,value in infractor["infraction_id"].items():
                        if key == "cost":
                            print("The fee is {}$".format(value))
                            paid = input("Has the infractor paid the fee? Enter a valid option:\nY - yes\nN - no\n->")
                            while not paid == "Y" or paid == "N":
                                paid = input("Has the infractor paid the fee? Enter a valid option:\nY - yes\nN - no\n->")
                            else:
                                if paid == "Y":
                                    db.remove(infractor)
                                else:
                                    continue
    elif menu == 3:
        print("Registered infractors:")
        for infractor in db:
            for key, value in infractor.items():
                print("\n\nPerson Information:")
                if key == "name": 
                    print(key, value)
                elif key == "last_name":
                    print (key,value)
                print("\n\nInfraction Information:")
                if key == "infraction_id": 
                    for key, value in infractor["infraction_id"].items():
                        print (key,value)
                print("\n\nOfficer Information:")
                if key == "officer": 
                    for key,value in infractor["officer"].items():
                        print (key,value)
        else:
            print("There are no registered fees")
    elif menu == 4:
        break
    else:
        continue