"""
Задача 20
Задайте список. Напишите программу, которая определит,
присутствует ли в заданном списке строк некое число.
Пример:
["qwe", "asd", "12", "qwe", "2"], 2 -> True
["qwe", "asd", "qwe", "681"], 7 -> False
["qwe", "asd", "qwe", "0"], 0 -> True
"""

import my_Lib as my
from functools import reduce

print('Определякем наличие заданного числа в списке:')

lst = "Oнo 2 и кoнeчнo, 14 пoнятнo, 63 oнo 257 чтo-либo кaк, и нe 9 кaк-либo".split()

while True:
    numb_find = my.get_InputNumber(txt='\nВведите число для поиска', end='-')
    if my.check_exit(numb_find):
        break
    result_find = reduce(lambda res, elem: res or elem == str(numb_find), lst, False)
    print(f'{lst}, {numb_find} - {result_find}')
