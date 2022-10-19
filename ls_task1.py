""""
Задача 1
Заданы числа - сформировать список кортежей из квадратов четных чисел
Пример: - [1 2 3 5 8 15 23 38] => [(2, 4), (8, 64), (38, 1444)]

# Варианты реализации:
# result = [(el, el ** 2) for el in map(int, lst) if el % 2 == 0]
# result = [(el, el ** 2) for el in map(int, lst) if not el % 2]
# result = [(el, el ** 2) for el in filter(lambda el: not el % 2, map(int, lst))]
# result = map(lambda el: (el, el ** 2),
#              filter(lambda el: not el % 2,
#                     map(int, lst)))
# print(f'{lst} => ', end='')
# print(*result)
"""

print('\nФормируем список кортежей из квадратов четных чисел заданной в файле последовательности:')

numbers = ''.join('5, 6, 9, 4, 8, 11, 1, 9, 12, 3'.split()).split(',')
open("fil_numbers", 'w').close()

with open("fil_numbers", 'a') as fil:
    for el in numbers:
        fil.write(el)
        fil.write('\n')

with open("fil_numbers") as fil:
    data = fil.read()

tuple_lists = ("1 2 3 5 8 15 23 38", data)

for lst in tuple_lists:
    lst = lst.replace('\n', ' ').split()
    result = list(map(lambda el: (el, el ** 2),
                      filter(lambda el: not el % 2,
                             map(int, lst))))

    print(f'{lst} => {result}')
