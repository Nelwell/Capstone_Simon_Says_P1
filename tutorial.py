# module to handle tutorial-related instructions
import time
import colorama
import transitions
import pattern_builder
from text_formatting import Bold_text
from colorama import Fore  # https://www.youtube.com/watch?v=u51Zjlnui4Y
import webbrowser



colorama.init()  # enables easy-calling of colors

general_instruction = f'\n{Fore.RESET}Overview:\nJust like the classic Simon Says game from the 70s, the goal is to ' \
                      f'repeat Simon\'s \npattern, which will be displayed as a set of colors ({Fore.RED}R, ' \
                      f'{Fore.GREEN}G, {Fore.BLUE}B, {Fore.RESET}or {Fore.YELLOW}Y{Fore.RESET}).  Each time \n' \
                      f'you successfully match the pattern you\'ll move to the next round and the pattern \n' \
                      f'will get longer.'


def instruction():
    print(general_instruction)
    see_video = input('\nWould you like to see a short (45 sec) video of the classic game? Y or Press Enter to \n'
                      'continue with the tutorial. ').upper()
    if see_video == 'Y':
        webbrowser.open('https://www.youtube.com/watch?v=vLi1qnRmpe4')  # opens up link to youtube video
        input('Press Enter when finished watching. ')
        time.sleep(.5)
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
        conclude_tutorial()  # ends tutorial after second round
    print(f'\n{Fore.LIGHTRED_EX}{Bold_text.BOLD}ROUND {stage} ', end='')
    time.sleep(1)
    print(f'{Fore.RESET}- This is what round you\'re in', end='')
    time.sleep(5)
    print('', end='\r')
    while True:
        pattern_builder.pattern_builder(colors, simon_pattern)  # calls function to create simon's pattern
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
        # if doesn't match
        print('\nIncorrect pattern, but for tutorial purposes let\'s continue. This would normally result in a '
              '\"Game Over\".\n')
        time.sleep(3)

    simon_round(stage, colors, player_pattern)  # passes player data to simon


def conclude_tutorial():
    input('This concludes the tutorial. Press Enter to return to the game. ')
    print(f'{Fore.LIGHTBLUE_EX}{Bold_text.BOLD}{transitions.introduction}')
