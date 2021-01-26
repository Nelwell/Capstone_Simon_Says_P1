from datetime import datetime, date, time

today = date.today()
print(today)

tomorrow = date(2021, 1, 19)
print(tomorrow)

next_week = date.fromisoformat('2021-01-25')
print(next_week)

right_now = datetime.now()
print(right_now)

print(right_now.timestamp())

my_date = datetime.fromtimestamp(1600000000)
print(my_date)
