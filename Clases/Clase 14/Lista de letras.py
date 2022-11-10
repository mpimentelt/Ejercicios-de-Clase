def search_letter(letter,list):
    if letter == list[len(list)-1]:
        return letter
    list = list.remove(list[len(list)-1])
    return search_letter(letter,list)


def main():
    list = ["a", "b", "c", "d", "e"]
    letter = input("Please enter a letter: ").lower()
    inlist = search_letter(letter,list)
    print(inlist)

main()
