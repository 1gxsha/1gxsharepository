# -- coding: utf-8 --
def compare(a,b,c):
    if a == b and a == c and b == c:
        print("3")
    elif a == b or a == c or b == c:
        print("2")
    else:
        print("0")
compare(int(input()),int(input()),int(input()))