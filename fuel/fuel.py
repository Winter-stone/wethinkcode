class OperandError(Exception):
    pass

while True:
    guage = input('Fraction: ')
    try:
        for i in guage:
            if not i.isdigit() and i != "/":
                raise OperandError
        tank = eval(guage)

    except OperandError:
        pass
    except ZeroDivisionError:
        continue
    except ValueError:
        pass
    except NameError:
        pass
    else:
        tank = tank * 100
        if 0 <= tank <= 100:
            if tank <= 1:
                print('E')
            elif tank >= 99:
                print('F')
            else:
                print(f'{round(tank)}%')
            break
        else:
            pass
