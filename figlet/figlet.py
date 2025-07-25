from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

random_font = Figlet(font=f'{random.choice(figlet.getFonts())}')

if len(sys.argv) < 2:
    text = input('Input: ').strip()
    print('Output: ',random_font.renderText(text))
elif len(sys.argv) > 1:
    if len(sys.argv) < 3:
        sys.exit('Invalid Usage')
    elif sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit('Invalid Usage')
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid Usage')
    else:
        chosen_font = Figlet(font = f'{sys.argv[2]}')
        text = input('Input: ').strip()
        print('Output: ',chosen_font.renderText(text))
