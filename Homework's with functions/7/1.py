# -- coding: utf-8 --
def Massiv(x):
        l = [1,2,3,4,5,6,7,8,9,10]
        maximum = max(l)
        minimum = min(l)
        for i in range(len(l)):
          if l[i] == maximum:
            l[i] = minimum
          elif l[i] == minimum:
            l[i] = maximum
        print(l)
Massiv(int(input()))
