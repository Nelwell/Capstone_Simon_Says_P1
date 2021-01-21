""" This is a simon says text-based game. Follow Simon's pattern for as long as possible.
One error will result in game over. """

import time
import colorama
import transitions
import tutorial
import pattern_builder
from text_formatting import Bold_text
from colorama import Fore  # https://www.youtube.com/watch?v=u51Zjlnui4Y


colorama.init()  # enables easy-calling of colors


def main():
    stage = 0
    colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    simon_pattern = []
    time.sleep(.5)
    print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}{transitions.introduction}')
    beginner = input(f'{Fore.RESET}Would you like to go through the tutorial? Y or N ').upper()
    if beginner == 'Y':
        tutorial.instruction()
    elif beginner == 'N':
        time.sleep(2)
        simon_round(stage, colors, simon_pattern)
    else:
        print('Please choose Y or N')


# creates random color pattern, gets longer each call
def simon_round(stage, colors, simon_pattern):
    stage += 1
    print(f'\n{Fore.LIGHTRED_EX}{Bold_text.BOLD}ROUND {stage}', end='')
    time.sleep(1.5)
    print('', end='\r')
    while True:
        pattern_builder.pattern_builder(colors, simon_pattern)
        player_round(stage, colors, simon_pattern)  # calls function to handle player's turn


# allows player input for an attempt to match simon's color pattern
def player_round(stage, colors, simon_pattern):
    countdown = ['Ready', 'Set', 'GO']
    for count in countdown:
        time.sleep(.50)
        if count == 'GO':
            print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}!', end='')
        else:
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
