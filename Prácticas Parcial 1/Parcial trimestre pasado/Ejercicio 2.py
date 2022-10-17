def get_max_wealth(accounts):
    max_wealth = 0
    for lista in accounts:
        if sum(lista) > max_wealth:
            max_wealth=sum(lista)
    return max_wealth

def main():
    accounts = [
        [1,2,3],
        [1,2,3]
    ]
    max_wealth = get_max_wealth (accounts)
    print (max_wealth)

main()