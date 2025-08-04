import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if ip.count('.') == 3:
        octets = re.search(r"^(.+)\.(.+)\.(.+)\.(.+)$", ip)
        for i in range(1, 5):
            try:
                if int(octets.group(i)) > 255 or 0 > int(octets.group(i)) or (octets.group(i).startswith('0') and len(octets.group(i)) > 1):
                    return False
            except ValueError:
                return False
        else:
            return True
    else:
        return False



if __name__ == "__main__":
    main()