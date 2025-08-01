def main():
    greeting = input('Greeting: ').lstrip()
    pay = value(greeting)
    print(f"${pay}")

def value(greeting):
    if 'hello' in greeting.lower():
        pay = 0

    elif greeting.lower().startswith('h') and greeting.lower() != 'hello':
        pay = 20

    else:
        pay = 100
    return pay

if __name__ == "__main__":
    main()
