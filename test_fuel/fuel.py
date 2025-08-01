def main():
    gauge_tank = input('Fraction: ').split('/')
    fraction = convert(gauge_tank)
    if isinstance(fraction, int):
        fuel = gauge(fraction)
        print(fuel)

def convert(fraction):
    if int(fraction[0]) < 0 or int(fraction[1]) < 0:
        raise ValueError
    tank = int(fraction[0]) / int(fraction[1])

    return round(tank * 100)

def gauge(percentage):
    if 0 <= percentage <= 100:
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return f'{round(percentage)}%'
    else:
        pass

if __name__ == "__main__":
    main()
