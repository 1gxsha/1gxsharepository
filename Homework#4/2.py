# -- coding: utf-8 --
a=int(input())
b=int(input())
if a<b:
    for k in range(a,b+1,+1):
        print(k,end=",")
else:
    for k in range(a,b-1,-1):
        print(k,end=",")
