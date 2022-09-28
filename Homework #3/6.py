# -- coding: utf-8 --
def dits(x,y,x1,y1):
    if (x+y+x1+y1) % 2 == 0:
        print("Да")
    else:
        print("Нет")
dits(int(input()),int(input()),int(input()),int(input()))