def main():
    time = input('What time is it?: ').lower()
    meal = convert(time)

    if meal is not None:
        if 7.0 <= meal < 8.01:
            print('breakfast time')

        elif 12.0 <= meal < 13.01:
            print('lunch time')

        elif 18.0 <=meal < 19.01:
            print('dinner time')

        else:
            pass

def convert(time):
    time = time.strip().split(":")
    if len(time) > 1:
        if time[1][3:] == 'p.m.':
            time[0] = int(time[0]) + 12
        try:
            time_converted = int(time[0]) + (int(time[1][:2]) / 60)
        except ValueError as e:
            print(time)

        else:
            return time_converted

if __name__ == "__main__":
    main()
