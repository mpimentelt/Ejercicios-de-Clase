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
        menu = int(input("Welcome, please enter a valid option: \n1. Show inventory\n2. Make a purchase\n3. \n4. Exit"))
        if menu == 1:
            type = int(input("Which products would you like to view?:\n1. Mobiles\n 2. Laptops"))
            for types, brands in products.items():
                if type == 1:
                    type == types[0]
                for brands, list_products in brands.items():
                    print(brands)
                    for product in list_products:
                        id = product.get("id")
                        name = product.get("name")
                        price = product.get("price")
                        print("Product: {}\nId: {}\nPrice: {}".format(name, id, price))

main()