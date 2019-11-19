"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

INP_N = abs(int(input("Введите n: ")))
SUM_N = 0
for i in range(1, INP_N + 1):
    SUM_N += i
if SUM_N == int(INP_N * (INP_N + 1) / 2):
    print(f" {SUM_N} == {int(INP_N * (INP_N + 1) / 2)}, равенство выполняется")


def rec_sum_n(numb, sum_numb=0):
    """
    calculate sum numbers from 1 to numb
    """
    if numb == 0:
        return sum_numb
    else:
        sum_numb += numb
        numb -= 1
        return rec_sum_n(numb, sum_numb)


def equality(inp_numb):
    """
    check equality 1+2+...+n = n(n+1)/2
    """
    if rec_sum_n(inp_numb) == int(inp_numb * (inp_numb + 1) / 2):
        print(f" {rec_sum_n(inp_numb)} == {int(inp_numb * (inp_numb + 1) / 2)}, равенство выполняется")


equality(5)
