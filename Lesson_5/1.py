"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections


def counter_res():
    """
    Counter
    """
    comps = collections.Counter()
    num_comps = int(input("Введите количество компаний: "))
    for i in range(num_comps):
        cn = input("Введите название компании: ")
        cn_res = 0
        for j in range(1, 5):
            cn_res += int(input(f"Введите прибыль за {j} квартал: "))
        comps[cn] = int(cn_res / 4)
    aver = int(sum(comps.values()) / num_comps)
    print(f"Средняя прибыль: {aver}")
    print(f"Ниже среднего: {[k for k, v in comps.items() if v < aver]}")
    print(f"Выше среднего: {[k for k, v in comps.items() if v > aver]}")


def namedtuple_res():
    """
    namedtuple, defaultdict
    """
    comp = collections.namedtuple('company', 'name, s1, s2, s3, s4')
    comps = collections.defaultdict(int)
    num_comps = int(input("Введите количество компаний: "))

    for i in range(num_comps):
        company = comp(
            name=(input("Введите название: ")),
            s1=int(input("Введите прибыль за 1 квартал: ")),
            s2=int(input("Введите прибыль за 2 квартал: ")),
            s3=int(input("Введите прибыль за 3 квартал: ")),
            s4=int(input("Введите прибыль за 4 квартал: ")),
        )
        comps[company.name] = int((company.s1 + company.s2 + company.s3 + company.s4) / 4)
    aver = int(sum(el for el in comps.values()) / num_comps)
    print(f"Средняя прибыль: {aver}")

    for i in comps:
        if comps[i] > aver:
            print(f"{i} - прибыль выше среднего")
        else:
            print(f"{i} - прибыль ниже среднего")


# counter_res()
# namedtuple_res()
