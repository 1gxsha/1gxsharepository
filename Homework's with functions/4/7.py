#-*-coding: utf-8-*-
def factorial(n):
	multiplication=1
	summ=0
	for i in range(1,n+1):
		multiplication*=i
		summ+=multiplication
	print(summ)
factorial(int(input()))
