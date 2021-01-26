""" This is a Simon Says text-based game. Follow Simon's pattern for as long as possible.
One error will result in game over. """

import time
import webbrowser
import winsound
import colorama
import transitions
import pattern_builder
from text_formatting import Bold_text, general_instruction
from colorama import Fore, Back  # https://www.youtube.com/watch?v=u51Zjlnui4Y

colorama.init()  # enables easy-calling of colors


def main(tutorial_completed):
    stage = 0
    colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    simon_pattern = []
    time.sleep(.5)
    print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}{transitions.introduction}')
    for sound in transitions.intro_sound:
        time.sleep(.40)
        winsound.PlaySound(sound, winsound.SND_ASYNC)
    if not tutorial_completed:  # checks if player has been through tutorial already, skips question if so
        beginner = input(f'{Fore.RESET}Would you like to go through the tutorial? Y or N ').upper()
        if beginner == 'Y':
            tutorial_intro()
        elif beginner == 'N':
            time.sleep(2)
            simon_round(stage, colors, simon_pattern)
        else:
            print('Please choose Y or N')
            time.sleep(1.5)
            main(tutorial_completed)
    time.sleep(2.5)
    simon_round(stage, colors, simon_pattern)


# creates random color pattern, gets longer each call
def simon_round(stage, colors, simon_pattern):
    stage += 1
    print(f'\n{Fore.LIGHTRED_EX}{Bold_text.BOLD}ROUND {stage}', end='')
    time.sleep(2.25)
    print('', end='\r')
    while True:
        pattern_builder.pattern_builder(colors, simon_pattern)
        time.sleep(2)
        print('', end='\r')  # hides simon's pattern after set amount of time / https://stackoverflow.com/
        # questions/44565704/how-to-clear-only-last-one-line-in-python-output-console
        player_round(stage, colors, simon_pattern)  # calls function to handle player's turn


# allows player input for an attempt to match simon's color pattern
def player_round(stage, colors, simon_pattern):
    countdown = ['Ready', 'Set', 'GO']
    for count in countdown:
        time.sleep(.4)
        if count == 'GO':
            print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}!', end='')
        else:
            print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}...', end='')
    time.sleep(.3)
    print('', end='\r')
    player_turn = input('')
    player_pattern = ' '.join(player_turn.upper()).split()  # creates space between each char, then splits at each space
    if player_pattern == simon_pattern:  # checks for match against simon's color pattern
        winsound.PlaySound('audio\\correct.wav', winsound.SND_ASYNC)
        if stage < 3:
            print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}Correct!', end='')
        elif 2 < stage < 6:
            print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}Keep Going!', end='')
        elif 5 < stage < 10:
            print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}You\'re on fire!', end='')
        elif 9 < stage < 20:
            print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}Unstoppable!!', end='')
        elif stage > 19:
            print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}LEGENDARY!!!', end='')
        time.sleep(1.5)  # short delay before beginning next round
        print('', end='\r')
        transitions.next_round()
    else:
        game_over(stage)  # if doesn't match, calls game over function

    simon_round(stage, colors, player_pattern)  # passes player data to simon


# gives player option to play again or not
def game_over(score):
    winsound.PlaySound('audio\\incorrect.wav', winsound.SND_ASYNC)
    print(f'\n{Fore.BLACK}{Back.RED} Game Over {Back.RESET}')
    time.sleep(1.5)
    scoring(score)


def scoring(score):
    score -= 1  # makes your scores feel more awesome, score 0 still possible
    print(f'\n{Fore.BLUE}{Back.BLACK} Score this game: {score} {Fore.RESET}{Back.RESET}')
    time.sleep(1)
    with open('simon_scores.txt', 'a') as f:  # creates/opens file and puts in append mode
        f.write(f'{score} ')  # adds latest score to score sheet

    with open('simon_scores.txt') as f:  # opens file for reading
        scores = f.read()  # puts scoring data from txt file into list
    f.close()
    score_list = ' '.join(scores).split()
    print(f'\n{Fore.BLUE}{Back.BLACK} ---YOUR TOP 10 SCORES---\n')
    make_integers = sorted(([int(i) for i in score_list]), reverse=True)  # list comp to convert to integers and sort
    back_to_string_scores = [str(s) for s in make_integers]  # list comp to convert back to string for printing
    for index, s in enumerate(back_to_string_scores[:10]):  # prints high scores, numbered up to 10
        print(f' {index + 1}. {s}')
    time.sleep(1.5)
    play_again()


def play_again():
    just_one_more = input(f'{Fore.RESET}{Back.RESET}\nPlay again? Y or N ').upper()
    if just_one_more == 'Y':
        main(tutorial_completed=True)
    else:
        print('Thanks for playing!')
        exit()


'''*** Tutorial operations below ***'''


def tutorial_intro():
    print(general_instruction)
    see_video = input('\nWould you like to see a short (45 sec) video of the classic game? Y or Press Enter to \n'
                      'continue with the tutorial. ').upper()
    if see_video == 'Y':
        webbrowser.open('https://www.youtube.com/watch?v=vLi1qnRmpe4')  # opens up link to youtube video,
        # https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python
        input('Press Enter when finished watching. ')
        time.sleep(.5)
    transitions.next_round()
    stage = 0
    colors = ['R', 'G', 'B', 'Y']  # possible colors in simon pattern
    simon_pattern = []
    time.sleep(.5)
    tutorial_simon_round(stage, colors, simon_pattern)


# creates random color pattern, gets longer each call
def tutorial_simon_round(stage, colors, simon_pattern):
    if stage < 2:
        stage += 1
    else:
        conclude_tutorial()  # ends tutorial after second round
    print(f'\n{Fore.LIGHTRED_EX}{Bold_text.BOLD}ROUND {stage} ', end='')
    time.sleep(1)
    print(f'{Fore.RESET}- This is what round you\'re in', end='')
    time.sleep(3)
    print('', end='\r')
    while True:
        pattern_builder.pattern_builder(colors, simon_pattern)  # calls function to create simon's pattern
        time.sleep(1)
        print(f'{Fore.RESET}- This is Simon\'s pattern. Remember it.', end='')
        time.sleep(4)
        print('', end='\r')  # hides simon's pattern after set amount of time / https://stackoverflow.com/
        # questions/44565704/how-to-clear-only-last-one-line-in-python-output-console

        tutorial_player_round(stage, colors, simon_pattern)  # calls function to handle player's turn


# allows player input for an attempt to match simon's color pattern
def tutorial_player_round(stage, colors, simon_pattern):
    tutorial_countdown = ['Ready', 'Set', 'GO']
    for count in tutorial_countdown:
        time.sleep(.5)
        if count == 'GO':
            print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}!', end='')
        else:
            print(f'{Fore.LIGHTGREEN_EX}{Bold_text.BOLD}{count}...', end='')
    time.sleep(.4)
    print('', end='\r')
    player_turn = input(f'{Fore.RESET}Don\'t worry about capitalization or spaces. Enter your response now: ')
    player_pattern = ' '.join(player_turn.upper()).split()  # creates space between each char, then splits at each space
    if player_pattern == simon_pattern:  # checks for match against simon's color pattern
        winsound.PlaySound('audio\\correct.wav', winsound.SND_ASYNC)
        print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}Correct! It\'s a match!', end='')
        time.sleep(1.5)  # short delay before beginning next round
        print('', end='\r')
        transitions.next_round()
    else:
        # if doesn't match
        winsound.PlaySound('audio\\incorrect.wav', winsound.SND_ASYNC)
        print('\nIncorrect pattern, but for tutorial purposes let\'s continue. Normally, this would result in '
              f'\"Game Over\".\n')
        time.sleep(3.5)

    tutorial_simon_round(stage, colors, simon_pattern)  # passes player data to simon


def conclude_tutorial():
    input(f'{Fore.RESET}\nYou made it through the tutorial! In the real game, the pattern will continue '
          f'to \nget longer each round and rounds will continue indefinitely as long as you can match '
          f'\nthe pattern. How many rounds can you survive? Press Enter to continue with the game. ')
    main(tutorial_completed=True)


main(tutorial_completed=False)
