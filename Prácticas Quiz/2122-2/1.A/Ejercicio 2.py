def main(): 
    products = {
        "mobiles": {
            "Apple": [
                {
                    "id": 1,
                    "name": "iPhone 7",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "iPhone 8",
                    "price": 350
                },
                {
                    "id": 3,
                    "name": "iPhone Xr",
                    "price": 450
                },
                {
                    "id": 4,
                    "name": "iPhone Xs",
                    "price": 460
                },
                {
                    "id": 5,
                    "name": "iPhone 11",
                    "price": 900
                },
                {
                    "id": 6,
                    "name": "iPhone 12",
                    "price": 1100
                },
                {
                    "id": 7,
                    "name": "iPhone 13",
                    "price": 1300
                },
            ],
            "Samsung": [
                {
                    "id": 8,
                    "name": "Samsung Galaxy Beam",
                    "price": 150
                },
                {
                    "id": 9,
                    "name": "Samsung Galaxy S6",
                    "price": 200
                },
                {
                    "id": 10,
                    "name": "Samsung Galaxy S7",
                    "price": 300
                },
            ],
            "Xiaomi": [
                {
                    "id": 11,
                    "name": "Xiaomi Redmi Note 8",
                    "price": 250
                },
                {
                    "id": 12,
                    "name": "Xiaomi Redmi Note 8 Pro",
                    "price": 300
                },
            ]
        },
        "laptops": {
            "DELL": [
                {
                    "id": 13,
                    "name": "Dell Inspiron 15",
                    "price": 600
                },
                {
                    "id": 14,
                    "name": "Dell Latitude 14",
                    "price": 650
                },
            ],
            "MAC": [
                {
                    "id": 15,
                    "name": "MacBook Pro 13",
                    "price": 900
                },
                {
                    "id": 16,
                    "name": "MacBook M1",
                    "price": 1500
                },
            ]
        },
    }

    while True:
        menu = input("Welcome to our store, please enter a valid option:\n1. Show inventory\n2. Make a purchase\n3. Apply promotion\n4. Exit\n->")
        while not menu.isnumeric:
            menu = input("Welcome to our store, please enter a valid option:\n1. Show inventory\n2. Make a purchase\n3. Apply promotion\n4. Exit\n->")
        else:
            menu = int(menu)
            if menu == 1:
                categories = {1: "mobiles", 2: "laptops"}
                category_input = input("Please enter the type of product you would like to view:\n1. Mobiles\n2. Laptops\n->")
                while not category_input.isnumeric():
                    category_input = input("Please enter the type of product you would like to view:\n1. Mobiles\n2. Laptops\n->")
                else: 
                    category_input = int(category_input)
                    for category, brands in products.items():
                        if category == categories[category_input]:
                            for brand, product_list in brands.items():
                                print(f"\n{brand}")
                                for product in product_list:
                                    id = product["id"]
                                    name = product["name"]
                                    price = product["price"]
                                    print("Name: {}\nId: {}\nPrice: {}".format(name,id,price))
            elif menu == 2: 
                item_id = input("Enter the Id of the product you would like to buy: ")
                purchase = None
                while not item_id.isnumeric():
                    item_id = input("Enter the Id of the product you would like to buy: ")
                else: 
                    item_id = int(item_id)
                    for category, brands in products.items():
                        for brands, product_list in brands.items():
                            for product in product_list:
                                if product["id"] == item_id:
                                    purchase = product
                                    break
                if purchase:
                    client = {
                        "name": input("Please enter your full name: "),
                        "idcard": input("Please enter your id: "),
                        "item_id": item_id
                    }
                    print("********RECEIPT********")
                    print("Client information: ")
                    for key, value in client.items():
                        print("{}\t{}".format(key, value))
                    print("Product information: ")
                    for key,value in purchase.items():
                        print("{}\t{}".format(key, value))
                else: 
                    print ("Product not found")
            elif menu == 3:
                for category, brands in products.items():
                    for brands, product_list in brands.items():
                        for product in product_list:
                            name = product["name"]
                            print(product)
                            for i in name:
                                if i.isnumeric():
                                    product["promo"] = True
                                    print 
                                    break
                                else: 
                                    product["promo"] = False
                for category, brands in products.items():
                    for brand, product_list in brands.items():
                        print(f"\n{brand}")
                        for product in product_list:
                            id = product["id"]
                            name = product["name"]
                            price = product["price"]
                            if product["promo"] == True:
                                promo = product["promo"]
                                print("Name: {}\nId: {}\nPrice: {}\nPromo:{}".format(name,id,price,promo))
                            else: 
                                print("Name: {}\nId: {}\nPrice: {}".format(name,id,price))

            elif menu == 4:
                print("Thank you for your visit!")
                break
            else:
                print("Option not found")
                continue

main()