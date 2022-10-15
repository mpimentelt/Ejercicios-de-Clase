pathologies = {
    "Respiratory system": [
        {
            "id": 1,
            "name": "Cystic Fibrosis",
            "price": 300 	
        },
        {
            "id": 2,
            "name": "Emphysema",
            "price": 500
        },
        {
            "id": 3,
            "name": "Tuberculosis",
            "price": 450
        }
    ],
    "Nervous system": [
        {
            "id": 4,
            "name": "Parkinson",
            "price": 800 	
        },
        {
            "id": 5,
            "name": "Epilepsy",
            "price": 600
        }
    ],
    "Endocrine system": [
        {
            "id": 6,
            "name": "Diabetes",
            "price": 350 	
        },
        {
            "id": 7,
            "name": "Acromegaly",
            "price": 700
        },
        {
            "id": 8,
            "name": "Hashimoto’s thyroiditis",
            "price": 900
        }
    ],   
}
patients = []
while True:
    menu = input("Welcome to our site. Please enter a valid option:\n1. Register and payment\n2. View patients\n3. Exit")
    while not menu.isnumeric():
        continue
    else:
        menu = int(menu)
        if menu == 1:
            pathology_id = input("Please enter the id of the pathology you have: ")
            while not pathology_id.isnumeric():
                pathology_id = input("Please enter the id of the pathology you have: ")
            else: 
                pathology_id = int(pathology_id)
                register = None
                for systems, list_pathology in pathologies.items():
                    for pathology in list_pathology:
                        if pathology["id"] == pathology_id:
                            register = pathology
                            break
                if register: 
                    patient = {
                        "name": input("Please enter your first name: "),
                        "last_name": input("Please enter your last name: "),
                        "id_card": input("Please enter your id: "),
                        "pathology_id": pathology_id
                    }
                    id = patient["id_card"]
                    for n in id:
                        if id[len(id)-1] == id[len(id)-3]:
                            patient["discount"]="30%"
                    print("***********RECEIPT***********")
                    print("Patient information: ")
                    for key,value in patient.items():
                        print("{}\t{}".format(key,value))
                    for key,value in register.items():
                        print("{}\t{}".format(key,value))
                else: 
                    print("Pathology not found")
            patients.append(patient)
        elif menu == 2: 
            pathology_view = input("Please enter the id of the pathology you would like to view: ")
            while not pathology_view.isnumeric():
                pathology_view = input("Please enter the id of the pathology you have: ")
            else: 
                pathology_view = int(pathology_view)
                for systems, list_pathology in pathologies.items():
                    for pathology in list_pathology:
                        if pathology["id"] == pathology_view:
                            print("{} patients".format(pathology["name"]))
                            for patient in patients:
                                if patient["pathology_id"] == pathology_view:
                                    print("Full name: {} {}".format(patient["name"],patient["last_name"]))
                            else:
                                print("There are no patients with {}".format(pathology["name"]))
        elif menu == 3:
            break
        else:
            continue