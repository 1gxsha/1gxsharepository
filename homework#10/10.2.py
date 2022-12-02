print('objective2')
file1 = open("C:\Users\HUAWEI\OneDrive\Рабочий стол\Shapkin_Georgiy_у-223_Vvod2.txt","r")
file2 = open("C:\Users\HUAWEI\OneDrive\Рабочий стол\Shapkin_Georgiy_у-223_vivod2.txt","w+")
M = [int(x) for x in file1]
N = a[0]
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
file2.write(str(B) + '\n')
for i, row in enumerate(B):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
file2.write(B)
file2.close()
file1.close()
