vendor  = 50
while vendor > 0:
    print('Amount Due:', vendor)
    machine = int(input("Insert Coin: "))
    if machine  == 25 or machine  == 10 or machine == 5:
        vendor -= machine
    else:
        pass

print('Change Owed:', abs(vendor))

