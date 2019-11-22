"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

TMP_LST = []
for i in range(10):
    TMP_LST.append(randint(1, 9))
print(TMP_LST, '\n')

# v1
LST = TMP_LST.copy()
L1 = (min(LST))
LST.remove(min(LST))
L2 = (min(LST))
print(f"Минимальные елементы: {L1} и {L2}")

# v2
LST2 = TMP_LST.copy()
if LST2[0] < LST2[1]:
    LM1, LM2 = 0, 1
else:
    LM1, LM2 = 1, 0
for i in range(2, len(LST2)):
    if LST2[i] < LST2[LM1]:
        if LST2[LM1] < LST2[LM2]:
            LM2 = LM1
        LM1 = i
    elif LST2[i] < LST2[LM2]:
        LM2 = i
print(f"Минимальные елементы: {LST2[LM1]} и {LST2[LM2]}")
