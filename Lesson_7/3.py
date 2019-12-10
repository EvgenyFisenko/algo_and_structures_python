"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random
import timeit


def gen_list(len_lst):
    lst = [random.randint(0, 100) for _ in range(2 * len_lst + 1)]
    return lst


def find_median(lst):
    """
    вариант без сортировки
    (еще вариант: print(sorted(LST.copy())[len(LST) // 2]))
    """
    lt, rt = [], []
    for i in range(len(lst) // 2):
        lt.append(lst.pop(LST.index(min(lst))))
        rt.append(lst.pop(LST.index(max(lst))))
    rt.reverse()
    print(lt, LST, rt)
    return str(LST[0])


def shaker_sort(lst):
    """
    1.5084642000000001 при 100 элементах
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        for i in range(left, right):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        right -= 1
        for i in range(right, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
    return lst


LST = gen_list(5)
print(LST)
print(f"Медиана: {find_median(LST)}")


# LST_SH = gen_list(100)
# print(LST_SH)
# print(shaker_sort(LST_SH))
# print(f"Медиана: {shaker_sort(LST_SH)[(len(LST_SH) // 2)]}")
#
# print(timeit.timeit("shaker_sort(LST_SH)",
#                     setup="from __main__ import shaker_sort, LST_SH", number=1000))
