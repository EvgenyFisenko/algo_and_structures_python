"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

USR_OP = ''
while USR_OP != '0':
    try:
        USR_A = int(input("Первое число: "))
        USR_B = int(input("Второе число: "))
    except ValueError:
        print("Допустимы только целые числа")
        continue
    USR_OP = input("Операция '+', '-', '*', '/' или 0 для выхода: ")
    if USR_B == 0 and USR_OP == '/':
        print("Деление на 0 невозможно")
        continue
    if USR_OP == '+':
        print(USR_A + USR_B)
    elif USR_OP == '-':
        print(USR_A - USR_B)
    elif USR_OP == '*':
        print(USR_A * USR_B)
    elif USR_OP == '/':
        print(round(USR_A / USR_B, 2))
    elif USR_OP == '0':
        print("Выход по нажатию 0")
        break
    else:
        print("Ошибка. Допустимые операции: '+', '-', '*', '/'")


def rec_calc():
    try:
        inp_a = int(input("Первое число: "))
        inp_b = int(input("Второе число: "))
        usr_op = input("Операция '+', '-', '*', '/' или 0 для выхода: ")
        if inp_b == 0 and usr_op == '/':
            print("Деление на 0 невозможно")
            return rec_calc()
    except ValueError:
        print("Допустимы только целые числа")
        return rec_calc()
    if usr_op == '+':
        print(inp_a + inp_b)
    elif usr_op == '-':
        print(inp_a - inp_b)
    elif usr_op == '*':
        print(inp_a * inp_b)
    elif usr_op == '/':
        print(round(inp_a / inp_b, 2))
    elif usr_op == '0':
        print("Выход по нажатию 0")
        return None
    else:
        print("Ошибка. Допустимые операции: '+', '-', '*', '/'")
    return rec_calc()


# rec_calc()
