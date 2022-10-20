""""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
import my_Lib as my


# Генератор чисел Фибоначчи
def gen_fibo(negative=None):
    a, b = 0, 0
    negative = -1 if negative else 1
    while True:
        temp = 1 if b == 0 else a
        a, b = b, temp + b * negative
        yield a


# Рекурсивная функция получения чисел Фибоначчи для n >= 0
def get_fibo(n):
    if n < 0: return (-1) ** (n - 1) * get_fibo(-n)
    if n < 2: return n
    return get_fibo(n - 2) + get_fibo(n - 1)


# n = int(input('Введите число -> '))
# print(list(map(int, [get_fibo(i) for i in range(-n, n + 1)])))
#
# exit()

M = dict([(0, 0), (1, 1)])


def fib(n):
    if n < 0: return (-1) ** (n - 1) * fib(-n)
    if n in M: return M[n]
    M[n] = fib(n - 1) + fib(n - 2)
    return M[n]


n = int(input('Введите число -> '))
print(list(map(int, [fib(i) for i in range(-n, n + 1)])))

exit()

# Рекурсивная лямбда получения чисел Фибоначчи для любых n, в т.ч. и < 0
fb = lambda n: n < 0 and (-1) ** (n - 1) * fb(-n) or n > 1 and fb(n - 2) + fb(n - 1) or n

# =============================================================
# Основное тело программы
# =============================================================
print('Формируем список чисел Фибоначчи для заданного k -> [-f(k), f(k-1), -3, 2, -1, 1, 0, 1, 1, 2, ... f(k)]')

# Вариант-2 с использованием рекурсии
while True:
    number = my.get_InputNumber(txt='\nВведите число', end='-')
    if my.check_exit(number):
        break

    print(f'\nдля k = {number} -> ', end='')
    print(list(map(int, [fb(i) for i in range(-number, number + 1)])))

exit()

# Вариант-1 с использованием генератора последовательности
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
