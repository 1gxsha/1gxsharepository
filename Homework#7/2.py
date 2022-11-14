# -- coding: utf-8 --
import statistics
num = []
for i in range(10):
    num.append(int(input()))
s=statistics.mean(num)
for i in range(10):
    if num[i]>s:
        num[i]=1
print(num)
