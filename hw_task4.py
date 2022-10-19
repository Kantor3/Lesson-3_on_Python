""""
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
from functools import reduce

print('Ищем произведение пар чисел в списке')
tuple_lists = ([1.1, 1.2, 3.1, 5, 10.01],
               [2.5, 3.69, 5.05, 6.11],
               [2.5, 3.99, 5.11, 9.7, 3.741],
               [1.11, 5.81, 6.3, 8.7, 3.2, 2.078, 7.42])

for lst in tuple_lists:
    # Алгоритм в одну строку - опять
    result = round(reduce(lambda a, b: a if a % 1 > b % 1 else b, lst) % 1 -
                   reduce(lambda a, b: a if b % 1 == 0 or a % 1 < b % 1 else b, lst) % 1, 5)
    print(f'{lst} => {result}')