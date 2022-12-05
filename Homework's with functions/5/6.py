#_*_coding: utf-8_*_
def gsh(n):
    a=[]
    summ=0
    while n!=0:
	summ+=n
	n=int(input())
	a.append(n)
    print(summ/len(a))
gsh(int(input()))
