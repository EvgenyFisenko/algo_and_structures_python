"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

На примере задачи 2-2:
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5)
"""


import cProfile
import sys
import timeit
import time as t


sys.setrecursionlimit(1000000)


def timer_dec(dec_func):
    def tmp(*arg):
        st_time = t.time() * 1000
        result = dec_func(*arg)
        time = t.time() * 1000 - st_time
        print(f"Время выполнения: {time:.9f} мс")
        return result
    return tmp


# @timer_dec
def rec_count(numb, even=0, odd=0):
    """
    O(N)
    """
    if numb == 0:
        return even, odd
    else:
        if (numb % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        numb = numb // 10
        return rec_count(numb, even, odd)


# @timer_dec
def lst_count(numb):
    """
    O(N)
    """
    return len([el for el in map(int, str(numb)) if el % 2 == 0]), len(
        [el for el in map(int, str(numb)) if el % 2 != 0])


# @timer_dec
def numb_count(numb):
    """
    O(N)
    """
    even_cnt, odd_cnt = 0, 0
    while numb != 0:
        if (numb % 10) % 2 == 0:
            even_cnt += 1
            numb = numb // 10
        else:
            odd_cnt += 1
            numb = numb // 10
    return even_cnt, odd_cnt


# print(f"rec_count {rec_count(34560**200)}")  # Время выполнения: 7.980957031 мс
# print(10 * "---")
# print(f"lst_count {lst_count(34560**200)}")  # Время выполнения: 0.996093750 мс
# print(10 * "---")
# print(f"numb_count {numb_count(34560**200)}")  # Время выполнения: 0.997314453 мс


# При запуске декораторы лучше убрать

# cProfile.run("rec_count(34560**200)")  # 912 function calls (4 primitive calls) in 0.002 seconds
# cProfile.run("lst_count(34560**2000)")  # 8 function calls in 0.006 seconds
# cProfile.run("numb_count(34560**2000)")  # 4 function calls in 0.075 seconds

# При запуске декораторы лучше убрать
# print(timeit.timeit("rec_count(34560)", setup="from __main__ import rec_count"))  # 1.3654115
# print(timeit.timeit("lst_count(34560)", setup="from __main__ import lst_count"))  # 2.7209778
# print(timeit.timeit("numb_count(34560)", setup="from __main__ import numb_count"))  # 0.9207863

print(timeit.timeit("rec_count(34560**200)", number=1, setup="from __main__ import rec_count"))  # 0.0015570
print(timeit.timeit("lst_count(34560**200)", number=1, setup="from __main__ import lst_count"))  # 0.0004588
print(timeit.timeit("numb_count(34560**200)", number=1, setup="from __main__ import numb_count"))  # 0.0009218


# 1.На малых числах собственный декоратор и cProfile не показательны.
# 2.При одинаковой сложности алгоритма необходимо учитывать константу.
# 3.Рекурсивный алгоритм ожидаемо проигрывает по скорости, по причине большого количества
# вызовов (высоты стека вызовов), алгоритм основанный на генераторах(lst_count) проигрывает
# по скорости алгоритму полного перебора(numb_count) так как имеет вдвое большую сложность,
# однако если верить timeit, то на больших числах он окажется быстрее.
