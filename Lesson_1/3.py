# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

USER_X1 = float(input("A(x= "))
USER_Y1 = float(input("A(y= "))
USER_X2 = float(input("B(x= "))
USER_Y2 = float(input("B(y= "))

K = (USER_Y1 - USER_Y2) / (USER_X1 - USER_X2)
B = USER_Y2 - K * USER_X2

print(f'y = {round(K,2)}x + {round(B,2)}')
