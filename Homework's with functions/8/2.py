# -- coding: utf-8 --
def GSH(m1,m2,m3,s1,s2,x1,x2,s3,x3):
    x1 = int(input("Введите количество элементов в первом списке "))
    m1 = []
    m2 = []
    m3 = []
    for i in range(x1):
       m1.append(int(input()))
    s1,s2,s3 = 0,0,0
    for i in range(x1):
       s1 += m1[i]
    print("Сумма элементов первого списка равна:",s1)
    print("Среднее арифметическое первого списка равно",s1/x1)
    x2 = int(input("Введите количество элементов во втором списке "))
    for j in range(x2):
       m2.append(int(input()))
    for j in range(x2):
       s2 += m2[j]
    print("Сумма элементов второго списка равна:",s2)
    print("Среднее арифметическое второго списка равно",s2/x2)
    x3 = int(input("Введите количество элементов в третьем списке "))
    for k in range(x3):
       m3.append(int(input()))
    for k in range(x3):
       s3 += m3[k]
    print("Сумма элементов третьего списка равна:",s3)
    print("Среднее арифметическое первого списка равно",s3/x3)
GSH(int(input()))
