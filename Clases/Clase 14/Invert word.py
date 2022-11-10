def invert_word(word,index):
    if index == 0:
        return word[index]
    return word[index] + invert_word(word, index-1)

def main():
    word = input("Please enter a word")
    index = len(word)
    print(invert_word(word,len(word)-1))

main()