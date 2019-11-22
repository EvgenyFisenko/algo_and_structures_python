"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

LST = []
for i in range(10):
    LST.append(randint(1, 9))
print(LST, '\n')

# v1
if LST.index(min(LST)) < LST.index(max(LST)):
    LT, RT = LST.index(min(LST)), LST.index(max(LST))
else:
    LT, RT = LST.index(max(LST)), LST.index(min(LST))
print(f"Границы: {LST[LT]} и {LST[RT]}, сумма: {sum(LST[LT + 1:RT])}")

# v2
MIN_IND, MAX_IND, SM = 0, 0, 0
for i in range(len(LST)):
    if LST[i] < LST[MIN_IND]:
        MIN_IND = i
    elif LST[i] > LST[MAX_IND]:
        MAX_IND = i
if MIN_IND < MAX_IND:
    LT2, RT2 = MIN_IND, MAX_IND
else:
    LT2, RT2 = MAX_IND, MIN_IND
for i in LST[(LT2 + 1):RT2]:
    SM += i
print(f"Границы: {LST[LT2]} и {LST[RT2]}, сумма: {SM}")
