"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque
from memory_profiler import profile
import timeit
CODING_TABLE = {}


# @profile
def build_tree(string):
    sorted_deque = deque(sorted(Counter(string).items(), key=lambda val: val[1]))
    if len(sorted_deque) != 1:
        while len(sorted_deque) > 1:
            new_el_weight = sorted_deque[0][1] + sorted_deque[1][1]
            new_el = {0: sorted_deque.popleft()[0], 1: sorted_deque.popleft()[0]}
            for ind, element in enumerate(sorted_deque):
                if new_el_weight > element[1]:
                    continue
                else:
                    sorted_deque.insert(ind, (new_el, new_el_weight))
                    break
            else:
                sorted_deque.append((new_el, new_el_weight))
    else:
        new_el_weight = sorted_deque[0][1]
        new_el = {0: sorted_deque.popleft()[0], 1: None}
        sorted_deque.append((new_el, new_el_weight))
    return sorted_deque[0][0]


# @profile
def encode(sorted_deque, path=''):
    if not isinstance(sorted_deque, dict):
        CODING_TABLE[sorted_deque] = path
    else:
        encode(sorted_deque[0], path=f'{path}0')
        encode(sorted_deque[1], path=f'{path}1')


# @profile
def print_encoded(my_str):
    encode(build_tree(my_str))
    print(f"Таблица значений: {CODING_TABLE}")
    print(my_str, end='  =  ')
    for el in my_str:
        print(CODING_TABLE[el], end=' ')
    print()


print_encoded('beep boop beer!')  # 00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001

# print(timeit.timeit("print_encoded('beep boop beer!')",
#                     setup="from __main__ import print_encoded", number=1000))  # 0.0912929

# Ни одна из функций данной реализации не вызывает инкримента памяти.
