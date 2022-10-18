def print_welcome():
    print("******** WELCOME ********")

def get_option(vehicles):
    for key, value in vehicles.items():
        print(f"\n{key}: ")
        for inner_key, inner_value in value.items():
            print(f"{inner_key}: {inner_value}")
    while True:
        option = input("\nPlease enter a valid option: ")
        if option.upper() == "A":
            return option
        elif option.upper() == "S":
            return option
        else: 
            continue

def get_client_data(option):
    client = {
        "id": input("Please enter your id: "),
        "vehicle type": option.upper()
    }
    hours=input("Please enter the amount of hours (in numbers) you would like to take: ")
    while not hours.isnumeric():
        hours=input("Please enter the amount of hours (in numbers) you would like to take: ")
    else:
        client["hours"]=int(hours)
    return client

def get_discount(client, vehicles):
    discount = 0
    if client["hours"]>3:
        discount += vehicles.get(client.get("vehicle type")).get("price per hour")*client["hours"]* 0.15
    return discount

def get_net_amount(vehicles,client,discount):
    return vehicles.get(client["vehicle type"]).get("price per hour")*client["hours"]-discount

def get_net_amount_A(vehicles,client,discount):
    if client["vehicle type"] == "A":
        return vehicles.get(client["vehicle type"]).get("price per hour")*client["hours"]-discount
    else: 
        return 0

def get_net_amount_S(vehicles,client,discount):
    if client["vehicle type"] == "S":
        return vehicles.get(client["vehicle type"]).get("price per hour")*client["hours"]-discount
    else: 
        return 0

def print_receipt(vehicles, client, total):
    print("******** RECEIPT ********")
    print("Id: ",client["id"])
    print("Vehicle type: ",vehicles.get(client.get("vehicle type")).get("description"))
    print("Total price to pay: {}$".format(total))

def get_discount_client(client):
    if client["hours"]>3:
        return client
    else:
        return None

def get_clientA(client):
    if client["vehicle type"] == "A":
        return client
    else:
        return None

def get_clientS(client):
    if client["vehicle type"] == "S":
        return client
    else:
        return None

def print_final_day(clients, net_amount, net_amount_A, net_amount_S, discount_clients, clientsA, clientsS):
    print("****** DAY STATISTICTS ******")
    print("Total amount of clients: ",len(clients))
    print("Total amount of clients for automatic: ", len(clientsA))
    print("Total amount of clients for synchronous: ", len(clientsS))
    print("Total amount of clients with discount: ", len(discount_clients))
    if len(clientsA) == 0:
        print("Average payments for automatic: 0$")
    else:
        print("Average payments for automatic: {}$".format(net_amount_A/len(clientsA)))
    if len(clientsS) == 0:
        print("Average payments for synchronous: 0$")
    else: 
        print("Average payments for synchronous: {}$".format(net_amount_S/len(clientsS)))
    print("Total payments: {}$".format(net_amount))

def main():
    print_welcome()
    vehicles_dict = {
        "A": {
            "description": "automatic",
            "price per hour": 2500
        },
        "S": {
            "description": "synchronous",
            "price per hour": 3500
        }
    }
    clients=[]
    discount_clients = []
    clientsA = []
    clientsS = []
    net_amount = 0
    net_amount_A = 0
    net_amount_S = 0
    while True: 
        option = get_option(vehicles_dict)
        client = get_client_data(option)
        clients.append(client)
        clientA = get_clientA(client)
        if not clientA == None:
            clientsA.append(clientA)
        clientS = get_clientS(client)
        if not clientS == None:
            clientsS.append(clientS)
        discount = get_discount(client, vehicles_dict)
        discount_client = get_discount_client(client)
        if not discount_client == None:
            discount_clients.append(discount_client)
        total = get_net_amount(vehicles_dict,client,discount)
        net_amount += total
        totalA = get_net_amount_A(vehicles_dict,client,discount)
        net_amount_A += totalA
        totalS = get_net_amount_S(vehicles_dict,client,discount)
        net_amount_S += totalS
        print_receipt(vehicles_dict, client, total)
        if input("Would you like to add another client? Y-yes or N-no").capitalize() == "N":
            break
    print_final_day(clients, net_amount, net_amount_A, net_amount_S, discount_clients, clientsA, clientsS)

main()