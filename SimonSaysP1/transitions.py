# transition variables
import colorama
from colorama import Fore
import winsound

colorama.init(autoreset=False)

introduction = """
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
  *                                                             *
*              CAN YOU MATCH SIMON\'S COLOR PATTERN?               *
  *                                                             *
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    """

# Store colors in variables - https://stackoverflow.com/questions/27311276/python-colorama-assign-color-code-to-variable
color_names = ['RED', 'GREEN', 'BLUE', 'YELLOW']
red_text = getattr(Fore, color_names[0])
green_text = getattr(Fore, color_names[1])
blue_text = getattr(Fore, color_names[2])
yellow_text = getattr(Fore, color_names[3])
set_text_color = [red_text, green_text, blue_text, yellow_text]

round_transition = '***************************************************************************************************'

intro_sound = ['audio\\red_sound.wav',
                'audio\\green_sound.wav',
                'audio\\yellow_sound.wav',
                'audio\\blue_sound.wav']


# displays transition pattern between rounds
def next_round():
    color_pos = 0
    for color in range(60):
        print(f'{set_text_color[color_pos]}\b{round_transition}')  # changes color per loop to create round transition
        if color_pos <= 2:
            color_pos = color_pos + 1
        else:
            color_pos = 0
