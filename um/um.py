import re

def main():
    print(count(input("Text: ")))

def count(s):
    count = 0
    um = s.split(",")
    for i in um:
        word = re.sub(r"\W", " ", i)
        if 'um' in word.strip().lower():
            string = word.split(" ")
            for um in string:
                if um.lower() == 'um':
                    count +=1
    return count

if __name__ == "__main__":
    main()
