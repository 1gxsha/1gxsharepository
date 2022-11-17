# -- coding: utf-8 --
import random
s = 0
num = 0
N = int(input("Ввод: "))
A = [[random.randrange(10) for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if A[i][j] <=0:
           continue
        if A[i][j] >0:
            num += 1
            s += A[i][j]
print("Сумма:", s)
print("Число:", num)
