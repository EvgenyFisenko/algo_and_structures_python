"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit
import cProfile


def find_simple_num(ind):
    """
    O(N2)
    """
    lst = [2]
    i = 3
    while len(lst) < ind:
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
        i += 1
    return lst[ind - 1]


def eratosfen(num):
    """
    O(n log(log n))
    """
    lst = [0] * 10000
    for i in range(10000):
        lst[i] = i
    lst[1] = 0
    ind = 2
    while ind < 10000:
        if lst[ind] != 0:
            j = ind * 2
            while j < 10000:
                lst[j] = 0
                j = j + ind
        ind += 1
    fin_lst = [el for el in lst if el != 0]
    return fin_lst[num - 1]


# print(find_simple_num(1000))
# print(eratosfen(1000))

# cProfile.run("find_simple_num(5)")  # 18 function calls in 0.000 seconds
# cProfile.run("eratosfen(5)")  # 5 function calls in 0.003 seconds

# cProfile.run("find_simple_num(1000)")  # 8921 function calls in 0.029 seconds
# cProfile.run("eratosfen(1000)")  # 5 function calls in 0.003 seconds

# print(timeit.timeit("find_simple_num(5)", number=1000, setup="from __main__ import find_simple_num"))  # 0.0021322
# print(timeit.timeit("eratosfen(5)", number=1000, setup="from __main__ import eratosfen"))  # 3.4588545

# print(timeit.timeit("find_simple_num(1000)", number=1, setup="from __main__ import find_simple_num"))  # 0.0270633
# print(timeit.timeit("eratosfen(1000)", number=1, setup="from __main__ import eratosfen"))  # 0.0034370000000000026

# 1. Добавляем в задачу пояснение: Искать i-е по счёту простое число будем в диапаззоне от 0 до 10000.
# 2. Скорость выполнения алгоритма решето Эратосфена проигрывает алгоритму пробного деления на малых числах,
# однако превосходит его с ростом количества элементов.
