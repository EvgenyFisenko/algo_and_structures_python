"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def hashing_substrings():
    tmp, hashed = set(), set()
    usr_str = input("Введите строку: ")
    for i in range(1, len(usr_str)):
        tmp.add(usr_str[i])
        tmp.add(usr_str[i:])
        tmp.add(usr_str[:-i])
        if usr_str[i:-i] != '':
            tmp.add(usr_str[i:-i])

    print(f"Колличество подстрок: {len(tmp)} ({tmp})")

    for i in tmp:
        hashed.add(hashlib.sha1(i.encode('utf-8')).hexdigest())

    return hashed


print(hashing_substrings())
