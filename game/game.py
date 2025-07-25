import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    else:
        if level > 0:
            secret = random.randint(1, level)
            break
        else:
            continue

while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            if guess > 0:
                if guess == secret:
                    print('Just right!')
                    break
                elif guess < secret:
                    print('Too small!')
                else:
                    print('Too large!')
            else:
                continue
