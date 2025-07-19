def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float("".join([i for i in d if i.isdigit() or i == "."]))


def percent_to_float(p):
    return float("".join([i for i in p if i.isdigit() or i == "."])) / 100

main()