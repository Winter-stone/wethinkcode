import sys

def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        print(count_lines(sys.argv))

def count_lines(argument):
    ext = argument[-1].split('.')
    if ext[-1] == 'py':
        lines = 0
        try:
            with open(argument[-1]) as file:
                for line in file:
                    if len(line.lstrip()) < 2:
                        pass
                    elif line.lstrip().startswith('#'):
                        pass
                    else:
                        lines += 1
                return lines

        except FileNotFoundError:
            sys.exit('File does not exist')

    else:
        sys.exit('Not a python file')

if __name__ == '__main__':
    main()
