# 5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

LETTER_1 = input("Первая буква: ")
LETTER_2 = input("Вторая буква: ")
START = ord("a") - 1

NUM_LETTER_1 = ord(LETTER_1) - START
NUM_LETTER_2 = ord(LETTER_2) - START
if NUM_LETTER_1 > NUM_LETTER_2:
    DIFF = NUM_LETTER_1 - NUM_LETTER_2
else:
    DIFF = NUM_LETTER_2 - NUM_LETTER_1

print(f"{LETTER_1}={NUM_LETTER_1}, {LETTER_2}={NUM_LETTER_2}, букв между ними:{DIFF - 1}")
