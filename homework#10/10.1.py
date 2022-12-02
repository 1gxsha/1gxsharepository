print('objective')
file1 = open("C:\Users\HUAWEI\OneDrive\Рабочий стол\Shapkin_Georgiy_у-223_Vvod.txt","r")
file2 = open("C:\Users\HUAWEI\OneDrive\Рабочий стол\Shapkin_Georgiy_у-223_vivod.txt","w+")
a = [int(x) for x in file1]
N = a[0]
A = [a[i:i+N] for i in range(1,len(a),N)]
file2.write(str(A) + '\n')
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
file2.write("Сумма:", s)
file2.write("Число:", num)
file2.close()
file1.close()
