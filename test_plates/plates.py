def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 1 < len(s) <= 6:
        if s.isalnum():
            if s[:2].isalpha():
                for item in range(len(s)):
                    if s[item].isdigit():
                        first_num = s[item]
                        s = s.split(s[item])
                        s[1] = first_num + s[1]
                        break
                else:
                    return True
                for letter in s[1]:
                    if letter.isalpha():
                        break
                    elif s[1][0] == "0":
                        break

                else:
                    return True
                
    return False


if __name__ == '__main__':
    main()
