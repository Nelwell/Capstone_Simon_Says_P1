""" This is a simon says text-based game. Follow Simon's pattern for as long as possible.
One error will result in game over. """

import getpass, os
import sys
import time
import random
import colorama
from colorama import Fore, Style  # https://www.youtube.com/watch?v=u51Zjlnui4Y

colorama.init(autoreset=True)  # automatically resets font attributes to default for subsequent prints


# provides terminal output-bolding functionality
class bold_text:
    BOLD = '\033[1m'  # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python


introduction = """
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
  *                                                             *
*                 CAN YOU MATCH SIMON\'S PATTERN?                  *
  *                                                             *
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    """


def main():
    stage = 0
    colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    simon_pattern = []
    time.sleep(.5)
    print(f'{Fore.LIGHTBLUE_EX}{bold_text.BOLD}{introduction}')
    time.sleep(2.5)
    print('', end='\r')
    simon_round(stage, colors, simon_pattern)


# creates random color pattern, gets longer each call
def simon_round(stage, colors, simon_pattern):
    stage = stage + 1
    time.sleep(.5)
    print(f'{Fore.LIGHTRED_EX}{bold_text.BOLD}ROUND {stage}', end='')
    time.sleep(1.5)
    print('', end='\r')
    while True:
        simon_pattern.append(random.choice(
            colors))  # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
        for color in simon_pattern:
            if color == 'R':
                time.sleep(.8)  # delay before displaying next color
                print(f'{Fore.RED}{bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
            elif color == 'G':
                time.sleep(.8)
                print(f'{Fore.GREEN}{bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
            elif color == 'B':
                time.sleep(.8)
                print(f'{Fore.BLUE}{bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
            else:
                time.sleep(.8)
                print(f'{Fore.YELLOW}{bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
        time.sleep(2)
        print('', end='\r')  # hides simon's pattern after set amount of time / https://stackoverflow.com/
        # questions/44565704/how-to-clear-only-last-one-line-in-python-output-console

        player_round(stage, colors, simon_pattern)  # calls function to handle player's turn


# allows player input for an attempt to match simon's color pattern
def player_round(stage, colors, simon_pattern):
    time.sleep(.25)
    print(f'{Fore.LIGHTGREEN_EX}{bold_text.BOLD}GO!')  # formats 'GO' message
    player_turn = input('')
    print('', end='\r')
    player_pattern = ' '.join(player_turn.upper()).split()  # creates space between each char, then splits at each space
    if player_pattern == simon_pattern:  # checks for match against simon's color pattern
        print(f'{Fore.LIGHTBLUE_EX}{bold_text.BOLD}We\'re just getting started', end='')
        time.sleep(1.5)  # short delay before beginning next round
        print('', end='\r')
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
