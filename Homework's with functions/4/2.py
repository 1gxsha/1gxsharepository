#-*-coding: utf-8-*-
def Gsh(a,b):
    if a<b:
	for i in range(a,b+1):
			print(i)
    else:
	for i in range(a,b-1,-1):
			print(i)
Gsh(int(input()),int(input()))
