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
    O(N2)
    """
    lst = [0] * (num ** 2)
    for i in range(num ** 2):
        lst[i] = i
    lst[1] = 0
    ind = 2
    while ind < num:
        if lst[ind] != 0:
            j = ind * 2
            while j < num ** 2:
                lst[j] = 0
                j = j + ind
        ind += 1
    fin_lst = [el for el in lst if el != 0]
    return fin_lst[num - 1]


print(f"Пятое по счету простое число: {find_simple_num(5)}")
print(f"Пятое по счету простое число: {eratosfen(5)}")

# cProfile.run("find_simple_num(5)")  # 18 function calls in 0.000 seconds
# cProfile.run("eratosfen(5)")  # 5 function calls in 0.000 seconds

# cProfile.run("find_simple_num(5000)")  # 53613 function calls in 0.686 seconds
# cProfile.run("eratosfen(5000)")  # 5 function calls in 21.559 seconds

# print(timeit.timeit("find_simple_num(5)", setup="from __main__ import find_simple_num"))  # 2.0589938
# print(timeit.timeit("eratosfen(5)", setup="from __main__ import eratosfen"))  # 7.3344758

# print(timeit.timeit("find_simple_num(1000)", number=10, setup="from __main__ import find_simple_num"))  # 0.2649625
# print(timeit.timeit("eratosfen(1000)", number=10, setup="from __main__ import eratosfen")) # 7.6449022

# Исходя из условия задачи, необходимо не просто искать все простые числа на промежутке до
# некоторого n, а находить именно i-тое простое число с использование решета Эратосфена и без.
# Текущая реализация алгоритма решета (eratosfen) сложностью O(N2), проигрывает по скорости
# выполнения алгоритму пробного деления (find_simple_num) сложностью O(N2) по причине не самого
# подходящего алгоритма для решения данной задачи или, возможно, не самой лучшей реализации алгоритма решета
# Эратосфена.
