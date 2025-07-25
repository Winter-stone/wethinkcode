names = []

while True:
    try:
        name = input('Name: ').strip().capitalize()
    except EOFError:
        if len(names) > 0:
            if len(names) > 2:
                names = ", ".join(names)
                names = names[-1::-1].replace(" ", ' dna ', 1)
                print("Adieu, adieu, to", names[-1::-1])

            else:
                names = " and ".join(names)
                print("Adieu, adieu, to", names)
        break

    else:
        if len(name) > 0:
            names.append(name)
