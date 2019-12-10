"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

NUMB_CNT, NUMERIC = 0, 0
while not NUMB_CNT or not NUMERIC:
    try:
        NUMB_CNT = int(input("Сколько чисел необходимо ввести: "))
        NUMERIC = int(input("Какую цифру будем искать: "))
    except ValueError:
        print("Ошибка. Введены некоректные данные.")
        continue
NUMERIC_CNT = 0
for i in range(1, NUMB_CNT + 1):
    try:
        USR_NUMB = int(input(f"Введите {i} число: "))
    except ValueError:
        print(f"Некорректные данные заменены на 0!")
        USR_NUMB = 0
    while USR_NUMB > 0:
        if USR_NUMB % 10 == NUMERIC:
            NUMERIC_CNT += 1
        USR_NUMB //= 10
print(f"Количество {NUMERIC}: {NUMERIC_CNT}шт")


def count_num_in_number(number, num, cnt=0):
    """
    возвращает количество повторений цифры в числе
    """
    if number == 0:
        return cnt
    else:
        if number % 10 == num:
            cnt += 1
        number //= 10
        return count_num_in_number(number, num, cnt)


def count_num_in_inp_numbers(numbers_cnt, num, num_cnt=0):
    """
    возвращает количество повторений цифры в запрашеваемых числах
    """
    if numbers_cnt == 0:
        return num_cnt
    else:
        numb = 0
        while not numb:
            try:
                numb = abs(int(input(f"Введите {numbers_cnt}-е число: ")))
            except ValueError:
                print("Только целые числа")
                continue
        num_cnt += count_num_in_number(numb, num)
        numbers_cnt -= 1
        return count_num_in_inp_numbers(numbers_cnt, num, num_cnt)


def numeric_search():
    """
    запрашивает количество вводимых чисел и искомую цифру
    возвращает сколько раз встречается определенная цифра в
    введенной последовательности чисел.
    """
    try:
        numbers_cnt = abs(int(input("Сколько чисел необходимо ввести: ")))
        numeric = abs(int(input("Какую цифру будем искать: ")))
        print(f"Цифра {numeric} встречается "
              f"{count_num_in_inp_numbers(numbers_cnt, numeric)} раз(а)")
    except ValueError:
        print("Ошибка. Введены некоректные данные.")
        numeric_search()


# numeric_search()
