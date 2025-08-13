import inflect
p = inflect.engine()
names = []

def main():
    while True:
        try:
            names.append(input('Name: ').strip().capitalize())
        except EOFError:
            print(convert(names))
            break

def convert(join_all):
    return f'''
Adieu, adieu, to {p.join(join_all)}'''

if __name__ == '__main__':
    main()
