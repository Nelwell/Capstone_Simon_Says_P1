import requests

question = input('Enter your question for the magic 8 ball: ')

magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

try:
    response = requests.get(magic_8_ball_url).json()
    answer = response['magic']['answer']
    print(f'The magic 8 ball says....    {answer}')
except Exception as e:
    print(e)  # for the developer to see what's going wrong during development, not for user to see
    print('Sorry, can\'t reach the 8ball right now')
