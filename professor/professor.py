import random

def main():
    level = get_level()
    problems = 10
    solved = 0
    while problems != 0:
        problems -= 1
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 3
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print('EEE')
                attempts -= 1
            else:
                if answer != x + y:
                    print('EEE')
                    attempts -= 1
                else:
                    solved += 1
                    break
            finally:
                if attempts == 0:
                    print(f'{x} + {y} = {x+y}')
                    break

    print('Score:', solved)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        else:
            if 0 < level < 4:
                return level
            else:
                continue

def generate_integer(level):
    if level == 1:
        ran = random.randint(0, 9)

    elif level == 2:
        ran = random.randint(10, 99)

    elif level == 3:
        ran = random.randint(100, 999)
    return ran

if __name__ == '__main__':
    main()
