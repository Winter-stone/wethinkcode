import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    valid = False
    for i in s.split(" "):
        if 'src' in i and 'youtube.com' in i and 'iframe' in s.split(" ")[0]:
            valid = True
            url = re.search(r"^.+\=(.+)$", i)
            quote = url.group(1).count('"')
            url = url.group(1).replace('"', "", quote).replace('b', '.b', 1).replace('.com/embed', "")
            url = re.search(r"^(.+)", url)
            url = re.sub(r"^(https?://)?(www\.)?", "https://", url.group(1).replace('></iframe>',""))

    if valid == False:
        return None
    return url

if __name__ == "__main__":
    main()
