"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

USR_INP = int(input("Введите число: "))
REV = 0
while USR_INP != 0:
    REV = int((REV + (USR_INP % 10) * 0.1) * 10)
    USR_INP = USR_INP // 10
print(f"{REV}")


def rec_reverse(numb, rev=0):
    """
    return reversed input number
    """
    if numb == 0:
        return rev
    else:
        rev = int((rev + (numb % 10) * 0.1) * 10)
        numb = numb // 10
        return rec_reverse(numb, rev)


# print(rec_reverse(348600))
