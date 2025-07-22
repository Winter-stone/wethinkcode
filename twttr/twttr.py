vowels = ['a','e','i','o','u']

name = input('Input: ')
for letter in name:
    if letter.lower() in vowels:
        name = name.replace(letter, "")
print('Output:',name)