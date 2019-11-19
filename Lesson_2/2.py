"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

US_NUMB = int(input("Введите число: "))
EVEN_CNT, ODD_CNT = 0, 0
while US_NUMB != 0:
    if (US_NUMB % 10) % 2 == 0:
        EVEN_CNT += 1
        US_NUMB = US_NUMB // 10
    else:
        ODD_CNT += 1
        US_NUMB = US_NUMB // 10
print(f"Четных:{EVEN_CNT}, нечетных:{ODD_CNT}")


def rec_count(numb, even=0, odd=0):
    """
    calculate even & odd numbers count with recursion
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


# print(f" (Четных, нечетных) = {rec_count(34560)}")
