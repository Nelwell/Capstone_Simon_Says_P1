# module to handle tutorial-related instructions
import time
import random
import colorama

from colorama import Fore, Style  # https://www.youtube.com/watch?v=u51Zjlnui4Y

import transitions
from text_formatting import Bold_text

colorama.init()  # enables easy-calling of colors

general_instruction = f'\n{Fore.RESET}Just like the classic Simon Says game from the 70s, the goal is to repeat ' \
                      f'Simon\'s \npattern, which will be displayed as a set of colors ({Fore.RED}R, {Fore.GREEN}G, ' \
                      f'{Fore.BLUE}B, {Fore.RESET}or {Fore.YELLOW}Y{Fore.RESET}).  Each time \n' \
                      f'you successfully match the pattern you\'ll move to the next round and the pattern \n' \
                      f'will get longer.  Press Enter when you\'re ready to move onto the first round.'


def instruction():
    print(general_instruction)
    input()
    transitions.next_round()
    stage = 0
    colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    simon_pattern = []
    time.sleep(.5)
    simon_round(stage, colors, simon_pattern)


# creates random color pattern, gets longer each call
def simon_round(stage, colors, simon_pattern):
    if stage < 2:
        stage += 1
    else:
        conclude_tutorial()
    print(f'\n{Fore.LIGHTRED_EX}{Bold_text.BOLD}ROUND {stage} ', end='')
    time.sleep(1)
    print(f'{Fore.RESET}- This is what round you\'re in', end='')
    time.sleep(5)
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
        time.sleep(1)
        print(f'{Fore.RESET}- This is Simon\'s pattern. Remember it.', end='')
        time.sleep(7)
        print('', end='\r')  # hides simon's pattern after set amount of time / https://stackoverflow.com/
        # questions/44565704/how-to-clear-only-last-one-line-in-python-output-console

        player_round(stage, colors, simon_pattern)  # calls function to handle player's turn


# allows player input for an attempt to match simon's color pattern
def player_round(stage, colors, simon_pattern):
    countdown = ['Ready', 'Set', 'GO']
    for count in countdown:
        time.sleep(.80)
        if count == 'GO':
            print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}!', end='')
        else:
            print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}...', end='')
    time.sleep(.50)
    print('', end='\r')
    player_turn = input(f'{Fore.RESET}Don\'t worry about capitalization or spaces. Enter your response now: ')
    player_pattern = ' '.join(player_turn.upper()).split()  # creates space between each char, then splits at each space
    if player_pattern == simon_pattern:  # checks for match against simon's color pattern
        print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}Good job!', end='')
        time.sleep(1.5)  # short delay before beginning next round
        print('', end='\r')
        transitions.next_round()
    else:
        print('Incorrect pattern')  # if doesn't match, calls game over function

    simon_round(stage, colors, player_pattern)  # passes player data to simon


def conclude_tutorial():
    input('This concludes the tutorial. Press Enter to continue to the game. ')
    print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}{transitions.introduction}')
