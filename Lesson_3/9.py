# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

N = 5
M = 10
EXT_LST = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(0, 10))
        print(f"{b[j]:4d}", end='')
    EXT_LST.append(b)
    print()

for i in range(M):
    print(f" ---", end='')
print()

MIN_LST = []
for i in range(M):
    mi = 0
    for j in range(N):
        if EXT_LST[j][i] < EXT_LST[mi][i]:
            mi = j
    MIN_LST.append(EXT_LST[mi][i])

for i in MIN_LST:
    print(f"{i:4d}", end='')
print('   |', max(MIN_LST))
