# -*- coding: utf-8 -*-
seconds = input()
minutes = int(seconds) / 60
seconds = int(seconds) % 60
hours = int(minutes) / 60
days = int(hours) / 24
print("Дней = ", days, "часов = ", hours, "минут = ", minutes, "секунд = ", seconds, sep=(" "))