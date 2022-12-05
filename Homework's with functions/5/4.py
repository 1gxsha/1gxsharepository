#_*_coding: utf-8_*_
def gsh(x,y):
	tan_procent=(10*x)/100
	days=0
	while x<y:
		x+=tan_procent
		days+=1
	print(days)
gsh(int(input()),int(input()))
