"""
Задача 19
Реализуйте алгоритм задания случайных чисел без использования
встроенного генератора псевдослучайных чисел.
"""


def gen_pseudorandom(A, B, M, r0=0):
    Xn = r0
    while True:
        yield Xn
        Xn = (A * Xn + B) % M


""" 
==============================================================================================
Основное тело программы
==============================================================================================
"""
import my_Lib as my
print('Создаем генреатор псевдослучайных чисел (ГПСЧ):')

while True:
    print("\nВведите параметры генератора.")
    gen_param = my.get_InputTuple("A =", "B =", "M =", "Количество сл.чисел =")
    if my.check_exit(gen_param):
        break
    A, B, M, cnt_number = gen_param

    rnd = gen_pseudorandom(A, B, M)

    for i, el in enumerate(rnd):
        print(f'{i+1} -> {el}')
        if i > cnt_number-2:
            break