name = input("camelCase: ").strip()
for letter in name[1:]:
    if letter.isupper():
        name = name.replace(letter, f'_{letter.lower()}')
print('snake_case:',name)
