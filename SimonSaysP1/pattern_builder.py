# logic to build Simon's pattern each round
import random
import time
import winsound
from colorama import Fore, Style
from text_formatting import Bold_text


def pattern_builder(colors, simon_pattern):
    # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
    simon_pattern.append(random.choice(colors))
    for color in simon_pattern:
        if color == 'R':
            time.sleep(.8)  # delay before displaying next color
            winsound.PlaySound('audio\\red_sound.wav', winsound.SND_ASYNC)  # plays called audio file
            print(f'{Fore.RED}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
        elif color == 'G':
            time.sleep(.8)
            winsound.PlaySound('audio\\green_sound.wav', winsound.SND_ASYNC)
            print(f'{Fore.GREEN}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
        elif color == 'B':
            time.sleep(.8)
            winsound.PlaySound('audio\\blue_sound.wav', winsound.SND_ASYNC)
            print(f'{Fore.BLUE}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
        else:
            time.sleep(.8)
            winsound.PlaySound('audio\\yellow_sound.wav', winsound.SND_ASYNC)
            print(f'{Fore.YELLOW}{Bold_text.BOLD}{color}{Style.BRIGHT}', end=' ')
    return simon_pattern
