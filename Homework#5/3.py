# -- coding: utf-8 --
n=int(input())
n=n>>1
#n=n//2
c=1
k=0
while c<=n:
    c*=2
    k+=1
print (k,c)
