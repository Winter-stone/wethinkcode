def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(name):
    if 1 < len(name) <= 6:
        if name.isalnum():
            if name[:2].isalpha():
                for item in range(len(name)):
                    if name[item].isdigit():
                        first_num = name[item]
                        name = name.split(name[item])
                        name[1] = first_num + name[1]
                        break
                else:
                    return name
                for letter in name[1]:
                    if letter.isalpha():
                        break
                    elif name[1][0] == "0":
                        break

                else:
                    return "".join(name)


main()