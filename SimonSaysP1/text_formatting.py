# Text formatting code

# provides terminal output-bolding functionality
from colorama import Fore


class Bold_text:
    BOLD = '\033[1m'  # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python


general_instruction = f'\n{Fore.RESET}Overview:\nJust like the classic Simon Says game from the 70s, the goal is to ' \
                      f'repeat Simon\'s \npattern, which will be displayed as a set of colors ({Fore.RED}R, ' \
                      f'{Fore.GREEN}G, {Fore.BLUE}B, {Fore.RESET}or {Fore.YELLOW}Y{Fore.RESET}).  Each time \n' \
                      f'you successfully match the pattern you\'ll move to the next round and the pattern \n' \
                      f'will get longer.'
