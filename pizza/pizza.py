import sys
import csv
from tabulate import tabulate
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

else:
    ext = sys.argv[-1].split('.')
    if ext[-1] == 'csv':
        lines = 0
        try:
            with open(sys.argv[-1]) as file:
                pizza = csv.reader(file)
                print(tabulate(pizza, headers = 'firstrow', tablefmt = 'grid'))
        except FileNotFoundError:
            sys.exit('File does not exist')

    else:
        sys.exit('Not a CSV file')
