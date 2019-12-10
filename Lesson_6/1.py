"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.

На примере задачи 2-2:
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5)
"""


from random import getrandbits
from sys import getsizeof
from memory_profiler import profile
from pympler import asizeof


@profile
def rec_count(numb, even=0, odd=0):
    if numb == 0:
        # print(getsizeof(even))  # 28
        # print(asizeof.asizeof(even))  # 32
        # print(getsizeof(odd))  # 28
        # print(asizeof.asizeof(odd))  # 32
        return even, odd
    else:
        if (numb % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        numb = numb // 10
        return rec_count(numb, even, odd)


@profile
def lst_count(numb):
    even = len([el for el in map(int, str(numb)) if el % 2 == 0])
    # print(getsizeof(even))  # 28
    # print(asizeof.asizeof(even))  # 32
    odd = len([el for el in map(int, str(numb)) if el % 2 != 0])
    # print(getsizeof(odd))  # 28
    # print(asizeof.asizeof(odd))  # 32
    return even, odd


@profile
def numb_count(numb):
    even_cnt, odd_cnt = 0, 0
    while numb != 0:
        if (numb % 10) % 2 == 0:
            even_cnt += 1
            numb = numb // 10
        else:
            odd_cnt += 1
            numb = numb // 10
    # print(getsizeof(even_cnt))  # 28
    # print(asizeof.asizeof(even_cnt))  # 32
    # print(getsizeof(odd_cnt))  # 28
    # print(asizeof.asizeof(odd_cnt))  # 32
    return even_cnt, odd_cnt


def craft_num():
    num = getrandbits(512)
    return num


NUMB = craft_num()
print(NUMB)

# print(getsizeof(7))  # 28
# print(asizeof.asizeof(7))  # 32

rec_count(NUMB)
lst_count(NUMB)
numb_count(NUMB)


#  Python 3.8.0, windows 10, 64 bit
#  В текущей реализации размер памяти, выделенный под переменные, оказался одинаковым, так как
#  во всех случаях это обычное число; getsizeof так же показал одинаково меньшее значение.
#  memory_profiler фиксирует небольшой (0.2 MiB) инкремент по памяти в рекурсивной реализации
#  алгоритма, что говорит о том, что рекурсия, в отличае от затрат по времени, тратит памяти
#  незначительно больше других реализаций, которые, в свою очередь, показывают 0.0 MiB инкремент.
