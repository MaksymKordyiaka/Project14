'''
Створити чотири класи, кожен з яких міститиме конструктор та прийматиме різну кількість атрибутів.
Помістити самі класи в список.

1.Передбачено, що три з чотирьох класів міститимуть методи з однаковими іменами (функціонал
методів- повернення атрибутів об’єкту). Знайти ці класи та помістити в окремий словник,
де ключем виступатиме посилання на сам клас, а значенням- посилання на сам метод.
Реалізація пошуку- через власну функцію.

2.Доповнити функціонал (завдання №1). Передбачено, що два з трьох класів також мають методи
з однаковими іменами (функціонал методів- не важливий). Реалізувати спосіб, при якому виклик
функції (завдання №1) повертатиме два словники з відповідними до (завдання №1) умовами.
Реалізація знаходиться в окремій функції.

Назви самих методів – довільні.
'''

class A:
    def __init__(self, a):
        self.a = a

    def method(self):
        return self.a

class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method(self):
        return self.a, self.b

class C:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def method_another(self):
        return self.a, self.b, self.c

class D:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

lst = [A, B, C, D]
def find_methods():
    dct = {}
    for clas in lst:
        if hasattr(clas, 'method'):
            method = getattr(clas, 'method')
            dct[clas] = method
    return dct
n = find_methods()
print(n)

def find_methods_extended():
    dct1 = {}
    dct2 = {}
    for clas in lst:
        if hasattr(clas, 'method'):
            method = getattr(clas, 'method')
            if clas in [A, B, C]:
                dct1[clas] = method
            if clas in [B, C]:
                dct2[clas] = method
    return dct1, dct2

n1, n2 = find_methods_extended()
print(n1)
print(n2)







