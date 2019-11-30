"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class HexNumber:
    def __init__(self, hex_num):
        self.hex_num = hex_num

    def __str__(self):
        return str(list(self.hex_num.upper()))

    def __add__(self, other):
        return HexNumber(hex(int(self.hex_num, 16) + int(other.hex_num, 16))[2:])

    def __mul__(self, other):
        return HexNumber(hex(int(self.hex_num, 16) * int(other.hex_num, 16))[2:])


HN1 = HexNumber('a2')
HN2 = HexNumber('c4f')
print(HN1, HN2)
print(HN1 + HN2)
print(HN1 * HN2)
