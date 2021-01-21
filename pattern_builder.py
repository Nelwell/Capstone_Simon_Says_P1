# logic to build Simon's pattern each round
import random
import time
from colorama import Fore, Style
from text_formatting import Bold_text


def pattern_builder(colors, simon_pattern):
    # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
    simon_pattern.append(random.choice(colors))
    for color in simon_pattern:
        if color == 'R':
            time.sleep(.8)  # delay before displaying next color
            print(f'{Fore.RED}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
        elif color == 'G':
            time.sleep(.8)
            print(f'{Fore.GREEN}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
        elif color == 'B':
            time.sleep(.8)
            print(f'{Fore.BLUE}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
        else:
            time.sleep(.8)
            print(f'{Fore.YELLOW}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
    time.sleep(2)
    print('', end='\r')  # hides simon's pattern after set amount of time / https://stackoverflow.com/
    # questions/44565704/how-to-clear-only-last-one-line-in-python-output-console
    return simon_pattern
