import csv
import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

else:
    old_ext = sys.argv[1].split('.')
    new_ext = sys.argv[-1].split('.')
    if old_ext[-1] == 'csv' and new_ext[-1] == 'csv':
        lines = 0
        students = []
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)

                for row in reader:
                    students.append({'name':row['name'], 'house':row['house']})

            with open(sys.argv[-1], 'w', newline='') as file:
                fieldnames = ['first', 'last', 'house']
                write = csv.DictWriter(file, fieldnames = fieldnames)
                write.writeheader()
                for row in students:
                    last_name, first_name = row['name'].split(',')
                    write.writerow({'first':first_name.lstrip(), 'last':last_name.lstrip(), 'house': row['house'].lstrip()})

        except FileNotFoundError:
            sys.exit('File does not exist')

    else:
        sys.exit('Not a CSV file')
