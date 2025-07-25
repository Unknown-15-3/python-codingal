from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is:", today)
print("The current time is:", now)

print("current year:", today.year)
print("current month:", today.month)
print("current day:", today.day)