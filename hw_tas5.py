""""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
import my_Lib as my


# Преобразование в двоичную систему счисления
def gen_fibo(negative=None):
    a, b = 0, 0
    negative = -1 if negative else 1
    while True:
        temp = 1 if b == 0 else a
        a, b = b, temp + b * negative
        yield a


# =============================================================
# Основное тело программы
# =============================================================
print('Формируем список чисел Фибоначчи для заданного k -> [-f(k), f(k-1), -3, 2, -1, 1, 0, 1, 1, 2, ... f(k)]')

while True:
    number = my.get_InputNumber(txt='\nВведите число', end='-')
    if my.check_exit(number):
        break

    fibo = gen_fibo()
    l_fibo_plus = [next(fibo) for _ in range(number)]
    fibo_rev = gen_fibo(negative=True)
    l_fibo_minus = [next(fibo_rev) for _ in range(number)]

    l_fibo = []
    [l_fibo.insert(0, el) for el in l_fibo_minus]
    l_fibo += l_fibo_plus

    print(f'\nдля k = {number} -> {l_fibo}')
