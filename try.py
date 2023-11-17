import datetime

a = "12:00"
b = "14:00"

time = datetime.datetime.strptime(a, '%H:%M')
print(time)
