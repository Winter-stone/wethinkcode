import random
import time

class DuplicatesError(Exception):
    pass

def main():
    while True:
        player_number = input("Enter Your Four Secret Digits: ")
        player_secret = get_player_secret(player_number)
        if player_secret:
            computer_secret = get_random_comp()
            break
        else:
            continue

    player_attempts = 0
    comp_attempts = 0
    get_feedback = []
    hold = []
    unpos_outcomes = []
    held = []

    while True:
        player_guess = input("Guess The Computer Secret Number: ")
        player_attempts += 1
        player_guess = player_guess.replace(" ", "")
        no_dups = no_duplicates(player_guess)
        for i in player_guess:
            time.sleep(.5)
            print(i, end = "")
        print(' Your Guess')

        if player_guess == "":
            print("Field Can't be empty")
            continue

        elif '0' in player_guess:
            print("Numbers Allowed From 1-9")
            continue

        elif len(player_guess) != len(computer_secret):
            print("Please Enter a Minimum of Four Digits")
            continue

        else:
            try:
                if not player_guess.isdigit():
                    raise ValueError

                elif no_dups == 'dups':
                    raise DuplicatesError

            except ValueError:
                print("Please Enter Integers Only")
                continue

            except DuplicatesError:
                print("No Duplicate Numbers Allowed")
                continue

            else:
                bulls, cows = game(computer_secret, player_guess)
                if player_guess != computer_secret:
                    print(f'''Bulls>> {bulls}, Cows>> {cows}
                    ''')

                else:
                    print("Congratilations, You Have Guessed The Secret Number", computer_secret)
                    print("Attempted Guesses", player_attempts)
                    again = input("Would You Like To Play Again? ").lower()
                    if 'y' in again:
                        get_feedback.clear()
                        player_attempts = 0
                        comp_attempts = 0
                        held.clear()
                        player_secret = get_player_secret()
                        computer_secret = get_random_comp()
                        continue
                    else:
                        print('Good Game 🤝')
                        break

        comp = get_random_comp()
        comp_attempts+=1
        sec = [str(x) for x in player_secret]

        for i in range(len(player_secret)):
            if comp[i] in get_feedback:
                continue
            elif comp[i] in player_secret:
                get_feedback.append(comp[i])

            elif not comp[i] in player_secret:
                hold.append(comp[i])

        if len(get_feedback) != 4:
            display = get_feedback.copy()
            for i in range(len(hold)):
                if hold[i] in display:
                    continue
                else:
                    display.append(hold[i])
                if len(display) == 4 and display != sec:
                    bulls, cows = game(sec, display)
                    for i in display:
                        time.sleep(.5)
                        print(i, end="")
                    print(" Computer's Guess")
                    time.sleep(.5)
                    print(f'''Computer Bulls>> {bulls}, Computer Cows>> {cows}
''')
            display.clear()
            hold.clear()

        elif len(get_feedback) == 4:
            for i in range(len(player_secret)):
                if get_feedback[i] != player_secret[i]:
                    unpos_outcomes.append(get_feedback[i])

                elif get_feedback[i] == player_secret[i]:
                    held.append(get_feedback[i])
                    position = get_feedback.index(get_feedback[i])

            if len(unpos_outcomes) > 3:
                random.shuffle(get_feedback)
                for i in get_feedback:
                    print(i, end="")
                    time.sleep(.5)
                print(" Computer Guess")
                unpos_outcomes.clear()

            elif len(unpos_outcomes) == 3:
                get_feedback.clear()
                random.shuffle(unpos_outcomes)
                unpos_outcomes.insert(position, held[0])
                get_feedback = unpos_outcomes.copy()
                for i in get_feedback:
                    print(i, end="")
                    time.sleep(.5)
                print(" Computer Guess")
                unpos_outcomes.clear()
                held.clear()

            elif len(unpos_outcomes) == 2:
                pos1, pos2 = find_position(get_feedback, player_secret)
                get_feedback[pos1], get_feedback[pos2] = get_feedback[pos2], get_feedback[pos1]
                for i in get_feedback:
                    print(i, end="")
                    time.sleep(.5)
                print(" Computer Guess")
                unpos_outcomes.clear()

            bulls, cows = game(sec,get_feedback)
            if get_feedback != sec:
                time.sleep(.5)
                print(f'''Computer Bulls>> {bulls}, Computer Cows>> {cows}''')

            elif get_feedback == sec:
                print("Computer Has Successfully Guessed Your Number", player_secret)
                print("After", comp_attempts, "Attempts")
                again = input("Would You Like To Play Again? ").lower()
                if "y" in again:
                    get_feedback.clear()
                    player_attempts = 0
                    comp_attempts = 0
                    held.clear()
                    player_secret = get_player_secret()
                    computer_secret = get_random_comp()
                    continue
                else:
                    print('Good Game 🤝')
                    break
        hold.clear()

def get_random():
    computer = random.randint(1111,9999)
    return str(computer)

def no_duplicates(number):
    for i in number:
        if number.count(i) > 1:
            return "dups"

def get_random_comp():
    while True:
        comp = get_random()
        no_dups = no_duplicates(comp)
        if no_dups == "dups":
            continue
        elif "0" in comp:
            continue
        else:return comp

def get_player_secret(player_number):
    no_dubs = no_duplicates(player_number)
    zero = '0'
    if no_dubs == "dups":
        print("No Duplicate Numbers Allowed")
    elif zero in player_number:
        print("Enter numbers only from 1-9")

    elif len(player_number) != 4:
        print("Please Enter a Minimum of Four Digits")
    else:
        try:
            if not player_number.isdigit():
                raise ValueError

            elif no_dubs == 'dubs':
                raise DuplicatesError

        except ValueError:
            print("Please Enter Integers Only")

        except DuplicatesError:
            print("No Duplicate Numbers Allowed")
        else:
            return player_number

def game(secret, guess):
    bulls = sum(1 for sec, gues in zip(secret, guess) if sec == gues)
    cows = sum(1 for gues in guess if gues in secret)- bulls
    return bulls, cows

def find_position(get_feedback, secret):
    find_position = []
    while True:
        for i in range(len(secret)):
            if get_feedback[i] != secret[i]:
                get_position = get_feedback.index(get_feedback[i])
                find_position.append(get_position)

        position = [str(x) for x in find_position]
        pos1 = position[0]
        pos2 = position[1]
        return int(pos1), int(pos2)


if __name__ == '__main__':
    main()