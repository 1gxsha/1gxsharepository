# -- coding: utf-8 --
a=int(input())
b=int(input())
r=b%2
if r==0:
    for k in range(b-1,a-1,-2):
        print(k,end=',')
else:
    for k in range(b,a-1,-2):
        print(k,end=',')
