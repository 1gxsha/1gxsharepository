# -- coding: utf-8 --
n = int(input())
min = n
hours = min // 60
min = n % 60
if n < 1440:
    print(hours, min, sep=":")
else:
    days = hours // 24
    hours %= 24
    print(days, "суток", hours, ":", min)