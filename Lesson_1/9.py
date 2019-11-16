# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

print("Вводятся три разных числа.")
INP_A = int(input("a = "))
INP_B = int(input("b = "))
INP_C = int(input("c = "))

if INP_A == INP_B or INP_A == INP_C or INP_B == INP_C:
    print("Числа должны быть РАЗНЫМИ по условию задачи.")
elif INP_B < INP_A < INP_C or INP_C < INP_A < INP_B:
    print(f"Среднее: {INP_A}")
elif INP_A < INP_B < INP_C or INP_C < INP_B < INP_A:
    print(f"Среднее: {INP_B}")
else:
    print(f"Среднее: {INP_C}")
