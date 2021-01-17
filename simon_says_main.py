""" This is a simon says text-based game. Follow Simon's pattern for as long as possible.
One error will result in game over. """

import time
import random
import colorama
from colorama import Fore, Style  # https://www.youtube.com/watch?v=u51Zjlnui4Y

colorama.init(autoreset=True)  # automatically resets font attributes to default for subsequent prints


# provides terminal output-bolding functionality
class bold_text:
    BOLD = '\033[1m'


def main():
    stage = 0
    colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    simon_pattern = []
    print('Can you match Simon\'s pattern?')
    simon_round(stage, colors, simon_pattern)


# creates random color pattern, gets longer each call
def simon_round(stage, colors, simon_pattern):
    stage = stage + 1
    print(f'Round {stage}')
    while True:
        simon_pattern.append(random.choice(colors))  # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
        for color in simon_pattern:
            if color == 'R':
                time.sleep(.8)  # delay before displaying next color
                print(f'{Fore.RED}{color}{Style.BRIGHT}', end=' ')
            elif color == 'G':
                time.sleep(.8)
                print(f'{Fore.GREEN}{color}{Style.BRIGHT}', end=' ')
            elif color == 'B':
                time.sleep(.8)
                print(f'{Fore.BLUE}{color}{Style.BRIGHT}', end=' ')
            else:
                time.sleep(.8)
                print(f'{Fore.YELLOW}{color}{Style.BRIGHT}', end=' ')
        time.sleep(2.5)
        print('', end='\r')  # hides simon's pattern after set amount of time / https://stackoverflow.com/
        # questions/44565704/how-to-clear-only-last-one-line-in-python-output-console

        player_round(stage, colors, simon_pattern)  # calls function to handle player's turn


# allows player input for an attempt to match simon's color pattern
def player_round(stage, colors, simon_pattern):
    ellipses = ['.', '.', '.']
    for i in ellipses:
        time.sleep(.3)
        print(f'{Fore.LIGHTMAGENTA_EX}{bold_text.BOLD}{i}{Style.BRIGHT}', end=' ')
    time.sleep(.4)
    print(f'{Fore.LIGHTMAGENTA_EX}{bold_text.BOLD}GO!{Style.BRIGHT}')
    player_turn = input('')
    player_pattern = ' '.join(player_turn.upper()).split()  # creates space between each char, then splits at each space
    if player_pattern == simon_pattern:  # checks for match against simon's color pattern
        print("Nice!")
        time.sleep(.5)  # short delay before beginning next round
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
