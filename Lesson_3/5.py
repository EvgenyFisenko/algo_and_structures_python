#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

LST = []
for i in range(10):
    LST.append(randint(-5, 2))
print(LST, '\n')

# v1
print(f"Максимальный отрицательный элемент: {max([i for i in LST if i < 0])}, "
      f"его позиция {LST.index(max([i for i in LST if i < 0]))}.")

# v2
MIN = 0
for i in LST:
    if i < MIN:
        MIN = i
GR = MIN
for i, el in enumerate(LST):
    if GR < el < 0:
        GR = el
        GRI = i
print(f"Максимальный отрицательный элемент: {GR}, "
      f"его позиция {GRI}.")
