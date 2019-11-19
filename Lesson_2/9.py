"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

USR_INP = input("Введите числа, разделяя их пробелом: ")
NUM_SUM = 0
for el in USR_INP.split(' '):
    TMP_SUM = 0
    for i in el:
        TMP_SUM += int(i)
        if TMP_SUM >= NUM_SUM:
            NUM_SUM = TMP_SUM
            GR_NUM = el
print(f"Последнее  введенное число наибольшее по сумме цифр: "
      f"{GR_NUM}, сумма его цифр: {NUM_SUM}")


def rec_max_sum(nums_str, num_sum=0, num_gr=0):
    """
    возвращает последнее наибольшее по сумме цифр число, и сумму его цифр
    """
    if len(nums_str) == 0:
        return num_gr, num_sum
    else:
        tmp_el = nums_str.split(' ')[0]
        tmp_sum = sum(map(int, tmp_el))
        if tmp_sum >= num_sum:
            num_sum = tmp_sum
            num_gr = tmp_el
        nums_str = nums_str[len(tmp_el) + 1:]
        return rec_max_sum(nums_str, num_sum, num_gr)


# print(rec_max_sum("111 222 33 44 55 6 70 811 00 02"))
