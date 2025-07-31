def main():
    name = input('Input: ')
    omitted = shorten(name)
    print('Output: ',omitted)


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter.lower() in vowels:
            word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()
