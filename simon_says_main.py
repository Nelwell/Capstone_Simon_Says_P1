""" This is a simon says text-based game. Follow Simon's pattern for as long as possible.
One error will result in game over. """

import time
import random
import colorama
import transitions
import tutorial
from colorama import Fore, Style  # https://www.youtube.com/watch?v=u51Zjlnui4Y


colorama.init(autoreset=False)  # enables easy-calling of colors


# provides terminal output-bolding functionality
class Bold_text:
    BOLD = '\033[1m'  # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python


def main():
    stage = 0
    colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    simon_pattern = []
    time.sleep(.5)
    print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}{transitions.introduction}')
    beginner = input('Would you like to go through the tutorial? Y or N ').upper()
    if beginner == 'Y':
        tutorial.instruction()
    elif beginner == 'N':
        time.sleep(2.5)
        simon_round(stage, colors, simon_pattern)
    else:
        print('Please choose Y or N')


# creates random color pattern, gets longer each call
def simon_round(stage, colors, simon_pattern):
    stage = stage + 1
    # time.sleep(.5)
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
    countdown = [3, 2, 1]
    for count in countdown:
        time.sleep(.40)
        print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}...', end='')
    time.sleep(.40)
    print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}GO!', end='')  # formats 'GO' message
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
        game_over()  # if doesn't match, calls game over function

    simon_round(stage, colors, player_pattern)  # passes player data to simon


# gives player option to play again or not
def game_over():
    print("Game Over")
    play_again = input("Play again? Y or N ").upper()
    if play_again == "Y":
        main()
    else:
        print('Thanks for playing!')
        exit()


main()
