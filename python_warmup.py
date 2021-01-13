# This program asks for your name and the month you were born in

from datetime import datetime

def get_name():
    name = input('Hello! What is your name? ')
    print (f'Good day to you,{name}! Now, let me ask you another question if I may...')
    return name

name = get_name()

# def get_birthday_month():
#     birthday_month = input(f'What month were you born in {name}? ').lower()
    
#     if birthday_month == 'august':
#         print(f'Happy Birthday month to you, {name}!')
#     else:
#         print('It\'s not quite your Birthday month yet.') 
#     return birthday_month

# birthday_month = get_birthday_month()

def check_bday_month_against_current_month():
    birthday_month = input(f'What month were you born in {name}? ').lower()
    current_month = datetime.now().strftime('%B').lower() # Gets current month's name - courtesy https://discuss.codecademy.com/t/can-i-display-the-month-name-instead-of-a-number/337967

    if birthday_month == current_month:
        print(f'Happy Birthday month to you, {name}!')
    else:
        print('It\'s not quite your Birthday month yet.')
    return birthday_month

is_it_your_bday_month = check_bday_month_against_current_month()