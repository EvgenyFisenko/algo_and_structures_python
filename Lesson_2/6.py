"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

import random

NUMB = random.randint(0, 100)
USR_ATP = 10
while USR_ATP != 0:
    try:
        USR_INP = int(input(f"Попыток осталось: {USR_ATP}. Введите число: "))
    except ValueError:
        print("Допустимы только числа от 1 до 100")
        continue
    if USR_INP < 0 or USR_INP > 100:
        print("Допустимы только числа от 1 до 100")
        continue
    elif USR_INP == NUMB:
        print(f"Поздравляем, вы угадали число {NUMB}!")
        break
    elif USR_INP > NUMB:
        print("Ваше число больше загаданного.")
    else:
        print("Ваше число меньше загаданного.")
    USR_ATP -= 1
else:
    print(f"У вас закончились попытки. Загаданное число {NUMB}")


def rec_game(numb, attempt):
    """
    :param numb: загаданное число
    :param attempt: количество попыток
    """
    if attempt == 0:
        print(f"У вас закончились попытки. Загаданное число {numb}")
        return numb
    else:
        try:
            usr_numb = int(input(f"Попыток осталось: {attempt}. Введите число от 1 до 100: "))
        except ValueError:
            print("Допустимы только целые числа")
            return rec_game(numb, attempt)
        if usr_numb < 0 or usr_numb > 100:
            print(f"Допустимы числа 1 до 100, минус попытка!")
        elif usr_numb == numb:
            print(f"Поздравляем, вы угадали число {numb}")
            return numb
        elif usr_numb > numb:
            print("Ваше число больше загаданного.")
        elif usr_numb < numb:
            print("Ваше число меньше загаданного.")
        attempt -= 1
    return rec_game(numb, attempt)


# rec_game(random.randint(0, 100), 10)
