""""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
from functools import reduce

print('Рассчитыаем сумму элементов на четных позициях списка чисел:')
tuple_lists = ([2, 3, 5, 9, 3],
               [6, 1, 4, 6, 8, 9, 5, 7],
               [1, 5, 6, 8, 3, 2, 7])

for lst in tuple_lists:
    sum_evenPos = reduce(lambda a, b: a + (b[1] if (b[0] + 1) % 2 == 0 else 0), enumerate(lst), 0)
    el_evenPos = list(el[1] for el in filter(lambda b: (b[0]+1) % 2 == 0, enumerate(lst)))
    print(f'{lst}, -> на нечётных позициях элементы {el_evenPos}, ответ: {sum_evenPos}')
