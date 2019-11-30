"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections


HEX_KEYS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hex_sum(hex_a, hex_b):
    hex_add = collections.deque('')
    hex_a = collections.deque(hex_a[:])
    hex_b = collections.deque(hex_b[:])
    while len(hex_a) != len(hex_b):
        if len(hex_a) > len(hex_b):
            hex_b.appendleft('0')
        else:
            hex_a.appendleft('0')
    hex_a.reverse()
    hex_b.reverse()

    digit = 0
    for i in range(len(hex_a)):
        sum_el = (HEX_KEYS[hex_a[i]] + HEX_KEYS[hex_b[i]] + digit) % 16
        digit = 1 if HEX_KEYS[hex_a[i]] + HEX_KEYS[hex_b[i]] > 15 else 0
        hex_add.appendleft(''.join([k for k, v in HEX_KEYS.items() if v == sum_el]))
        if i == len(hex_a) - 1 and digit == 1:
            hex_add.appendleft('1')
    return hex_add


def hex_mul(hex_a, hex_b):
    hex_a = collections.deque(hex_a)
    hex_b = collections.deque(hex_b)

    if len(hex_a) < len(hex_b):
        hex_a, hex_b = hex_b, hex_a
    hex_a.reverse()
    hex_b.reverse()

    hex_mult = []
    for el_b in range(len(hex_b)):
        lst_mul = []
        digit = 0
        for el_a in range(len(hex_a)):
            mul_el = ((HEX_KEYS[hex_b[el_b]] * HEX_KEYS[hex_a[el_a]] + digit) % 16)
            digit = (HEX_KEYS[hex_b[el_b]] * HEX_KEYS[hex_a[el_a]] + digit) // 16
            lst_mul.append((''.join([k for k, v in HEX_KEYS.items() if v == mul_el])))
            if el_a == len(hex_a) - 1 and digit:
                lst_mul.append(str(digit))
        hex_mult.append(list(reversed(lst_mul)))

    for i in range(1, len(hex_mult)):
        hex_mult[i].extend('0' * i)
        hex_mult[0] = hex_sum(''.join(hex_mult[0]), ''.join(hex_mult[i]))
    return hex_mult[0]


def hex_def_deque():
    """
    a, b = int(input("1ое:"), 16), int(input("2ое:"), 16)
    print(list(hex(a+b))[2:], list(hex(a*b))[2:])
    """
    hex_a = (input("Введите первое 16-ричное число: ").upper())
    hex_b = (input("Введите вторрое 16-ричное число: ").upper())
    print(f"{list(hex_a)} + {list(hex_b)} = {list(hex_sum(hex_a, hex_b))}")
    print(f"{list(hex_a)} * {list(hex_b)} = {list(hex_mul(hex_a, hex_b))}")


# hex_def_deque()
