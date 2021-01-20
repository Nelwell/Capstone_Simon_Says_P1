# module to handle tutorial-related instructions
import time
import random
import colorama

from colorama import Fore, Style  # https://www.youtube.com/watch?v=u51Zjlnui4Y

import transitions
from simon_says_main import Bold_text

colorama.init(autoreset=False)  # enables easy-calling of colors


def instruction():
    print('Hello')
    # stage = 0
    # colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    # simon_pattern = []
    # time.sleep(2.5)
    # simon_round(stage, colors, simon_pattern)


# creates random color pattern, gets longer each call
def simon_round(stage, colors, simon_pattern):
    if stage < 3:
        stage = stage + 1
    else:
        conclude_tutorial()
    print(f'\n{Fore.LIGHTRED_EX}{Bold_text.BOLD}ROUND {stage}', end='')
    time.sleep(1.5)
    print('', end='\r')
    while True:
        simon_pattern.append(random.choice(colors))  # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
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

        player_round(stage, colors, simon_pattern)  # calls function to handle player's turn


# allows player input for an attempt to match simon's color pattern
def player_round(stage, colors, simon_pattern):
    countdown = ['Ready', 'Set', 'GO']
    for count in countdown:
        time.sleep(.40)
        print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}...', end='')
    time.sleep(.40)
    print('', end='\r')
    player_turn = input('')
    player_pattern = ' '.join(player_turn.upper()).split()  # creates space between each char, then splits at each space
    if player_pattern == simon_pattern:  # checks for match against simon's color pattern
        print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}We\'re just getting started', end='')
        time.sleep(1.5)  # short delay before beginning next round
        print('', end='\r')
        transitions.next_round()
    else:
        print('Incorrect pattern')  # if doesn't match, calls game over function

    simon_round(stage, colors, player_pattern)  # passes player data to simon



def conclude_tutorial():
    input('This concludes the tutorial. Press Enter to continue the game. ')
    print(f'{Fore.LIGHTBLUE_EX}{bold_text.BOLD}{transitions.introduction}')

