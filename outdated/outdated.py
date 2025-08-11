calender = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
    time = input('Date: ').strip()
    if time.count('/') == 2:
        mon, day, year = time.split("/")
        try:
            if int(mon) <= 12 and int(day) <= 31 and len(year) == 4:
                print(f'{year}-{int(mon):02}-{int(day):02}')
                break
            else:
                continue
        except:
            continue


    elif len(time.split(',')) == 2:
        date, year = time.split(',')
        mon, day = date.split(" ")
        try:
            if mon in calender and int(day) <= 31 and len(year.strip()) == 4:
                print(f'{year.strip()}-{int(calender.index(mon)) + 1:02}-{int(day):02}')
                break
            else:
                continue
        except:
            continue
    else:
        continue
