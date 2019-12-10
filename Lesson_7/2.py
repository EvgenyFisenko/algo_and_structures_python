"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random
import timeit


def gen_list(len_lst):
    lst = [round(random.uniform(0, 50), 2) for _ in range(len_lst)]
    return lst


def merge_sort(lst):
    """
    0.20205220000000002 при 100 элементах
    Требует дополнительного места для хранения извлечённых списков.
    Проблемный адгоритм для больших наборов данных.
    """
    if len(lst) > 1:
        cnt = len(lst) // 2
        left = lst[:cnt]
        right = lst[cnt:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst


LST = gen_list(100)
print(LST)
print(merge_sort(LST))
print(timeit.timeit("merge_sort(LST)",
                    setup="from __main__ import merge_sort, LST", number=1000))
