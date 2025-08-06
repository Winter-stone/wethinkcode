import re

def main():
    time = input('Enter current time: ').strip().strip("''").strip('""')
    working = convert(time)
    print(working)

def convert(s):
    if 'to' not in s.lower():
        raise ValueError
    work = re.search(r"^(.+)to(.+)", s.lower())
    start_shift = work.group(1).upper().strip()
    end_shift = work.group(2).upper().strip()
    start = start_shift.upper().split(":")
    end = end_shift.upper().split(":")
    validate_min = end[-1].split(" ")
    valid_min = start[-1].split(" ")

    if len(validate_min[0]) == 1:
        end[-1] = '0' + end[-1]

    if len(valid_min[0]) == 1:
        start[-1] = '0' + start[-1]

    if len(validate_min[0]) > 2:
        raise ValueError
    elif len(valid_min[0]) > 2:
        raise ValueError

    if int(valid_min[0]) > 59:
        raise ValueError
    elif int(validate_min[0]) > 59:
        raise ValueError

    if len(start) > 1:
        if 'PM' in start[-1]:
            if int(start[0]) < 12:
                start[0] = str((int(start[0]) + 12))
            elif int(start[0]) > 12:
                raise ValueError
            start = ":".join(start)
            start = start.replace('PM', "")
        elif 'AM' in start[-1]:
            if int(start[0]) == 12:
                start[0] = '00'

            elif int(start[0]) > 12:
                raise ValueError
            else:
                start[0] = f'{int(start[0]):02d}'
            start = ":".join(start)
            start = start.replace('AM', "")

    elif len(start) < 2:
        start = start[0].split(" ")
        if 'PM' in start[-1]:
            if int(start[0]) < 12:
                start = str(int(start[0]) + 12)
                start = start + ":" + "00 "
            elif int(start[0]) > 12:
                raise ValueError
            else:
                start = start[0] + ":" + "00 "
        elif 'AM' in start[-1]:
            if int(start[0]) == 12:
                start[0] = '00'
            elif int(start[0]) > 12:
                raise ValueError
            else:
                start[0] = f'{int(start[0]):02d}'
            start = ":".join(start)
            start = start.replace('AM', "") + "00 "

    if len(end) > 1:
        if 'PM' in end[-1]:
            if int(end[0]) < 12:
                end[0] = str(int(end[0]) + 12)
            elif int(end[0]) > 12:
                raise ValueError
            end = ":".join(end)
            end = end.replace('PM', "")
        elif 'AM' in end[-1]:
            if int(end[0]) == 12:
                end[0] = '00'
            elif int(end[0]) > 12:
                raise ValueError
            else:
                end[0] = f'{int(end[0]):02d}'
            end = ":".join(end)
            end = end.replace('AM', "")

    elif len(end) < 2:
        end = end[0].split(" ")
        if 'PM' in end[-1]:
            if int(end[0]) < 12:
                end = str(int(end[0]) + 12)
                end = end + ":" + "00"
            elif int(end[0]) > 12:
                raise ValueError
            else:
                end = end[0] + ":" + '00'
        elif 'AM' in end[-1]:
            if int(end[0]) == 12:
                end[0] = '00'
            elif int(end[0]) > 12:
                raise ValueError
            else:
                end[0] = f'{int(end[0]):02d}'
            end = ":".join(end)
            end = end.replace('AM', "") + "00"

    if isinstance(start, list) or isinstance(end, list):
        raise ValueError
    else:
        return f'{start}to {end}'

if __name__ == "__main__":
    main()
