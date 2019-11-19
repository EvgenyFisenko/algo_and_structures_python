"""
4.	Найти сумму user_n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (user_n) вводится с клавиатуры.
"""

USR_N = int(input("Количество элементов: "))
SUM_N = 0
ROW_EL = 1
for i in range(USR_N):
    SUM_N += ROW_EL
    ROW_EL /= -2
print(f"Сумма {USR_N} элементов: {SUM_N}")


def rec_sum(user_n, sum_n=0, row_el=1):
    """
    calculate sum of user_n row elements
    """
    if user_n == 0:
        return sum_n
    else:
        sum_n += row_el
        row_el /= -2
        user_n -= 1
        return rec_sum(user_n, sum_n, row_el)


# print(rec_sum(3))
