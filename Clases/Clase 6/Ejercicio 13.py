currency_dict = {"Euro":"€", "Dollar": "$", "Yen": "¥"}
currency_input = input("Please enter a currency, eg: Euro, Dollar, Yen, etc")
print(currency_dict.get(currency_input.title(), "Currency not found"))