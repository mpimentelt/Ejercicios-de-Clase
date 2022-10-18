def is_prime(rif):
    number = int(rif[len(rif)-1])
    prime = True
    for x in range(2,number):
        if number%x == 0 or x<=1:
            prime = False
            break
    if prime:
        return True
    else: 
        return False

def main():
    products = {
        "Q": {
            "description": "químico",
            "price": 1000
        },
        "F": {
            "description": "farmacéutico",
            "price": 2500
        },
        "B": {
            "description": "biológico",
            "price": 4000
        },
    }
    clientsF=0
    clientsQ=0
    clientsB=0
    discountF=0
    discountQ=0
    discountB=0
    max_purchase=0
    rif_max_purchase=0
    total_day=0

    while True:
        rif = input("Please enter your rif: ")
        product_code = input("Please enter the code of the product you would like: \nQ - Químico\nF - Farmacéutico\nB - Biológico")
        payment_method = input("Please enter the method you would like to use for payment:\nC - Contado\nR - Crédito")
        net_amount = products[product_code].get("price")
        discount = 0
        taxes = 0
        if payment_method == "C":
            discount += net_amount*0.03
        if net_amount %2 == 0:
            discount += net_amount*0.02
        if is_prime(rif):
            discount += net_amount*0.05
        if product_code == "F":
            taxes += net_amount*0,12
        total = net_amount+taxes-discount
        if product_code == "F":
            clientsF+=1
            discountF+=discount
        if total > max_purchase:
            rif_max_purchase = rif
            max_purchase = total
        total_day += total
        print("****** RECEIPT ******")
        print("RIF: ", rif)
        print("Product: ", products[product_code].get("description"))
        print("Payment Method: ", payment_method)
        print("Discount: ", discount)
        print("Taxes: ", taxes)
        print("Total: ", total)
        if input("")== "N":
            break

    print("******* DAY STATISTICS *******")
    print("Clients Q", clientsQ)
    print("Clients F", clientsF)
    print("Clients B", clientsB)
    print("Discount Q", discountQ)
    print("Discount F", discountF)
    print("Discount B", discountB)
    print("Max purchase: ",max_purchase)
    print("Max purchase rif: ", rif_max_purchase)
    print("Total for the day: ", total_day)

main()