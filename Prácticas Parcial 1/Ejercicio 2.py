def print_welcome():
    print("***** Welcome *****")

def get_option(studies):
    for key,value in studies.items():
        for key_interno, value_interno in value.items():
            print(f"{key}   -   {value_interno}", end="") #arreglar acá la letra que está de más
        print("")
    return input("Please enter an option: ")

def get_client_data(study):
    client = {
        "id": input("Please enter your id: "),
        "age": input("Please enter your age: "), 
        "gender": input("Please enter your gender: "),
        "study": study
    }
    return client

def get_discounts(client,studies,client_number):
    discount = 0
    if client.get("gender") == "F" and int(client.get("age"))>55:
        discount += studies.get(client.get("study")).get("price")*0.25
    if client.get("gender") == "M" and int(client.get("age"))>65:
        discount += studies.get(client.get("study")).get("price")*0.25
    if not client_number%2 == 0: 
        discount += studies.get(client.get("study")).get("price")*0.02
    return discount

def get_net_amount (client, studies, discount):
    return studies.get(client.get("study")).get("price") - discount

def get_net_amount_U (client, studies, discount):
    if client.get("study") == "U":
        return studies.get(client.get("study")).get("price") - discount
    else:
        return 0

def get_net_amount_T (client, studies, discount):
    if client.get("study") == "T":
        return studies.get(client.get("study")).get("price") - discount
    else:
        return 0

def get_net_amount_F (client, studies, discount):
    if client.get("study") == "F":
        return studies.get(client.get("study")).get("price") - discount
    else:
        return 0

def print_invoice(client, studies, total):
    print("********RECEIPT********")
    print("Id card:", client.get("id"))
    print("Age: ", client.get("age"))
    print("Gender: ", client.get("gender"))
    print("Study: ", studies.get(client.get("study")).get("description"))
    print("Total price: ", total)

def get_clientsU (client):
    if client.get("study") == "U":
            return client

def get_clientsT (client):
    if client.get("study") == "T":
            return client

def get_clientsF (client):
    if client.get("study") == "F":
            return client

def print_final_day(clients, clientsU, clientsT, clientsF, total_discounts, total_amount, totalU, totalT, totalF):
    print("****** DAY STATISTICTS ******")
    print("Total amount of clients: {}".format(len(clients)))
    print("Total amount of clients for ultrasound: {}".format(len(clientsU)))
    print("Total amount of clients for tomography: {}".format(len(clientsT)))
    print("Total amount of clients for resonance: {}".format(len(clientsF)))
    print("Total amount of discounts: {}$".format(total_discounts))
    print("Total net amount: {}$".format(total_amount))
    print("Total net amount for ultrasound: {}$".format(totalU))
    print("Total net amount for tomography: {}$".format(totalT))
    print("Total net amount for resonance: {}$".format(totalF))
    print("Average of payments: {}$".format(total_amount/len(clients)))

def main():
    studies_dict = {
        "U": {
            "description": "ultrasonido",
            "price": 8900
        },
        "T": {
            "description": "tomografía",
            "price": 12640
        },
        "F": {
            "description": "resonancia",
            "price": 15600
        }
    }
    clients = []
    total_discount = 0
    total_net_amount = 0
    total_net_amountU = 0
    total_net_amountT = 0
    total_net_amountF = 0
    clientsU = []
    clientsT = []
    clientsF = []
    print_welcome()
    while True:
        option=get_option(studies_dict)
        client=get_client_data(option)
        clients.append(client)
        discount = get_discounts(client,studies_dict,len(clients))
        total_discount += discount
        total = get_net_amount(client,studies_dict,discount)
        total_net_amount += total
        totalU = get_net_amount_U(client,studies_dict,discount)
        total_net_amountU += totalU
        totalT = get_net_amount_T(client,studies_dict,discount)
        total_net_amountT += totalT
        totalF = get_net_amount_F(client,studies_dict,discount)
        total_net_amountF += totalF
        print_invoice(client,studies_dict,total)
        clientsU.append(get_clientsU(client))
        if None in clientsU:
            clientsU.remove(None)
        clientsT.append(get_clientsT(client))
        if None in clientsT:
            clientsT.remove(None)
        clientsF.append(get_clientsF(client))
        if None in clientsF:
            clientsF.remove(None)
        if input("Would you like to continue? Y - yes or N-No") == "Y":
            break
    
    print_final_day(clients, clientsU, clientsT, clientsF, total_discount, total_net_amount, total_net_amountU, total_net_amountT, total_net_amountF)


main()