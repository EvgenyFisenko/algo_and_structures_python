"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


class ListCar:
    __slots__ = ['speed', 'color', 'name', 'is_police']

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


class TupleCar:
    __slots__ = ('speed', 'color', 'name', 'is_police')

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False


CR = Car(200, 'black', 'car')
print(CR.__dict__)
print(asizeof.asizeof(CR))  # 552

LCR = ListCar(200, 'black', 'car')
print(LCR.__slots__)
print(asizeof.asizeof(LCR))  # 232

TCR = TupleCar(200, 'black', 'car')
print(TCR.__slots__)
print(asizeof.asizeof(TCR))  # 232

A, B, C = {}, [], ()
print(type(A), asizeof.asizeof(A))  # <class 'dict'> 64
print(type(B), asizeof.asizeof(B))  # <class 'list'> 56
print(type(C), asizeof.asizeof(C))  # <class 'tuple'> 40


#  Python 3.8.0, windows 10, 64 bit
#  Использование __slots__ = [] и __slots__ = () дает выигрыш по памяти в ~ 2,5 раза
#  по сравнению с __dict__, а они, в свою очередь, на малых данных дают одинаковый результат.
#  А т.к. под кортеж выделяется меньше памяти, можно предположить, что на больших
#  данных __slots__ = () будет выигрывать по использованию памяти и у __slots__ = [].
