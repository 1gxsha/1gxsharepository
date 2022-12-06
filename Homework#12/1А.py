# -- coding: utf-8 --
def add(n):
    if n > 0:
        print(n%10)
        print(' ')
        add(n//10)
add(int(input("Введите число: ")))