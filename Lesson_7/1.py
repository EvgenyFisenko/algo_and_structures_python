"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random
import timeit


def gen_list(len_lst):
    lst = [random.randint(-100, 100) for _ in range(len_lst)]
    return lst


def bubble_sort(lst):
    """
    0.37427170000000004 при 100 элементах
    """
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def bubble_sort_short(lst):
    """
    0.009977100000000003 при 100 элементах, так же
    0.006986599999999999 при 100 элементах, зависит от начальной упорядоченности массива
    Работает быстрее тк алгоритм останавливается раньше если обнаруживает что список отсортирован.
    Хорошо подходит для списков которым нужно всего несколько проходов.
    """
    exchanges = True
    num = len(lst) - 1
    while num > 0 and exchanges:
        exchanges = False
        for i in range(num):
            if lst[i] < lst[i + 1]:
                exchanges = True
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
        num = num - 1

    return lst


# LST = gen_list(100)
# print(LST)
# print(bubble_sort(LST))
# print(timeit.timeit("bubble_sort(LST)",
#                     setup="from __main__ import bubble_sort, LST", number=1000))

LST = gen_list(100)
print(LST)
print(bubble_sort_short(LST))
print(timeit.timeit("bubble_sort_short(LST)",
                    setup="from __main__ import bubble_sort_short, LST", number=1000))
