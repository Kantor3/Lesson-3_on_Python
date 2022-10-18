"""
Задача 21
Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
Пример:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
"""

from functools import reduce


def find_pos(first, second):
    occur_find = 1 if second == str_find else 0
    pos_find = first[0] if (first[1] == numb_occur - 1) and (occur_find == 1) else 0
    return tuple([a + b for a, b in zip(first, (1, occur_find, pos_find))])


print('Ищем позицию 2-го вхождения строки в списке:')
numb_occur = 2
reduce_init = (0,) * 3

tuple_lists = ((["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"),
               (["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], "йцу"),
               (["йцу", "фыв", "ячс", "цук", "йцукен"], "йцу"),
               (["123", "234", 123, "567"], "123"),
               ([], "123"),
               ("Oнo и кoнeчнo oнo и пoнятнo oнo и нe чтo-либo как и нe кaк-либo как чтo".split(), "как")
               )
for lst, str_find in tuple_lists:
    pos = reduce(find_pos, lst, reduce_init)[2]
    print(f'{lst}, ищем: "{str_find}", ответ: {pos}')

