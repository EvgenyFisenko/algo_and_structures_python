#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

TMP_LST = []
for i in range(10):
    TMP_LST.append(randint(1, 9))
print(f"Список:     {TMP_LST}")

# v1
LST = TMP_LST.copy()
MIN_I, MAX_I = LST.index(min(LST)), LST.index(max(LST))
print(f"min:{LST[MIN_I]} max:{LST[MAX_I]}", end=' ')
LST[MIN_I], LST[MAX_I] = LST[MAX_I], LST[MIN_I]
print(LST)

# v2
LST2 = TMP_LST.copy()
MIN_IND, MAX_IND = 0, 0
for i in range(len(LST2)):
    if LST2[i] < LST2[MIN_IND]:
        MIN_IND = i
    elif LST2[i] > LST2[MAX_IND]:
        MAX_IND = i
print(f"min:{LST2[MIN_IND]} max:{LST2[MAX_IND]}", end=' ')
TMP = LST2[MIN_IND]
LST2[MIN_IND] = LST2[MAX_IND]
LST2[MAX_IND] = TMP
print(LST2)
