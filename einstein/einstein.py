def einstein():
    c = 300000000**2
    while True:
        try:
            integer = int(input('m: '))
        except ValueError:
            print('Only Interger inputs are required')
        else:
            break
    return integer * c

print('E:',einstein())