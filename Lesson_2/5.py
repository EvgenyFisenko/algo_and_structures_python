"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

for a_num in range(32, 128):
    if a_num % 10 == 2:
        print('\n', end='')
    print(f"{a_num:>3}:{chr(a_num)} |", end=' ')


def rec_ascii(ascii_num):
    """
    recursively show ascii symbols from input to 127
    """
    if ascii_num == 128:
        return ascii_num
    else:
        if ascii_num % 10 == 2:
            print('\n', end='')
        print(f"{ascii_num:>3}:{chr(ascii_num)} |", end=' ')
        ascii_num += 1
        return rec_ascii(ascii_num)


print('\n')
# rec_ascii(32)
