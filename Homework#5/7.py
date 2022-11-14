# -- coding: utf-8 --
b=int(input())
a=int(input())
s=0
while a!=0:
    if a>b:
        s+=1
    b=a
    a=int(input())
print(s)
