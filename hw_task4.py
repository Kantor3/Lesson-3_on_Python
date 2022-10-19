""""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
import my_Lib as my


# Преобразование в двоичную систему счисления
def convert_deciNumb(numb10, base=2):
    str_bin = ''
    while numb10:
        str_bin = str(numb10 % base) + str_bin
        numb10 = numb10 // base
    return str_bin


# =============================================================
# Основное тело программы
# =============================================================
print('Преобразование десятичное число в двоичное')

while True:
    number = my.get_InputNumber(txt='\nВведите число', end='-')
    if my.check_exit(number):
        break

    print(f'{number} -> {convert_deciNumb(number)}')