"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random

INT_LEFT = int(input("Min int: "))
INT_RIGHT = int(input("Max int: "))
INT_RND = int(random() * (INT_RIGHT - INT_LEFT + 1) + INT_LEFT)
print(INT_RND)

FLOAT_LEFT = float(input("Min float: "))
FLOAT_RIGHT = float(input("Max float: "))
FLOAT_RND = random() * (FLOAT_RIGHT - FLOAT_LEFT) + FLOAT_LEFT
print(round(FLOAT_RND, 3))

STR_LEFT = input("Min letter: ")
STR_RIGHT = input("Max letter: ")
STR_RND = random() * (ord(STR_RIGHT) - ord(STR_LEFT)) + ord(STR_LEFT)
print(chr(int(STR_RND)))
