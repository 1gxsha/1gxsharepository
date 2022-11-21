# -- coding: utf-8 --
n=int(input())
f=1
s=0
for k in range(1,n+1):
    f*=k
    s+=f
print(s)
