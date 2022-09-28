# -- coding: utf-8 --
def year(visokos):
    if ((visokos%4 == 0) and visokos%100 != 0) or visokos%400 == 0:
        print("Да")
    else:
        print("Нет")
year (int(input()))