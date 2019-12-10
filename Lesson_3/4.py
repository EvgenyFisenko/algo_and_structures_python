# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint

LST = []
for i in range(10):
    LST.append(randint(1, 5))
print(LST, '\n')

# v1
OFT, CNT = 0, 0
for i in LST:
    if LST.count(i) > CNT:
        CNT = LST.count(i)
        OFT = i
print(f"Чаще всего встречается {OFT}; {CNT} раз(а).")

# v2
OFT2, CNT2 = 0, 0
for i in range(len(LST) - 1):
    TMP_CNT = 0
    for j in range(len(LST)):
        if LST[i] == LST[j]:
            TMP_CNT += 1
    if TMP_CNT > CNT2:
        CNT2 = TMP_CNT
        OFT2 = LST[i]
print(f"Чаще всего встречается {OFT2}; {CNT2} раз(а).")
